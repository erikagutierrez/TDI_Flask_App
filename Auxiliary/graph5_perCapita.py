'''get california counties, population'''

import sqlite3

conn = sqlite3.connect('/Users/erikagutierrez/Desktop/DataScience/TDI/TechTest/stateRx.db')
cur = conn.cursor()

qs1 = """SELECT County, sum(pop_total)
From dof_dru_pop_1970_2050_csya_wide
Where `year` = '2016'
Group by County """

'''make dictionary of ca counties, population, opioid rate'''
all_rows = cur.execute(qs1)

ls_county = list() #58 counties
ls_total_pop = list()
for tup in all_rows :
    ls_county.append(tup[0])
    ls_total_pop.append(tup[1])

#create list of opioid pop in each county. 1% is standard estimate.
#https://www.cdc.gov/drugoverdose/data/overdose.html
#deaths in 2016: https://www.vox.com/policy-and-politics/2017/9/5/16255040/opioid-epidemic-overdose-death-2016
# odds of dying: 64000/2M w/ disease. = .032 === 3.2% chance of death
# 1/33 people die of opioid addiction every year.

#opioid deaths a county, * 33 = county_addicted_rate

qs2 = """SELECT County, Counts
FROM `CA_All Opioid Overdose_2016_2018-02-05`"""

#source of calcs:
all_rows = cur.execute(qs2)

ls_opioid_pop = [round(people*.02) for people in ls_total_pop]

# ls_opioid_pop = list()
# for tup in all_rows :
#     opioid_addicted_rate = int(tup[1]) * 33
#     ls_opioid_pop.append(opioid_addicted_rate)

#find treatment gap per county:

qs3 = """SELECT County, COUNT(1)
from `Physician_Locator_2018-02-04T03-06-56`
where `State` = 'California' AND LENGTH(COUNTY) > 1 AND County <> 'GRAYS HARBOR'
group by County """

'''make dictionary of ca counties, population, opioid rate'''
all_rows = cur.execute(qs3)

ls_total_MD = [0 for county in ls_county] #initialize list with zeros

for tup in all_rows :
    county = tup[0]
    num_MDs = int(tup[1])
    county_index = ls_county.index(county)
    ls_total_MD[county_index] = num_MDs

# total number of patients treated by MDs, assuming they have 100 patients, only 66% of doctors accept medicaid.
patient_capacity_byMDs = [doctor*100 for doctor in ls_total_MD]
print('patient capacity:', patient_capacity_byMDs)
treatment_gap = [x-y for x,y in zip(ls_opioid_pop, patient_capacity_byMDs)]
print('treatment gap', treatment_gap)

print('opioid pop', ls_opioid_pop)
print('total pop in county:', ls_total_pop)
'''heat map'''
from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper
)
from bokeh.palettes import Inferno256 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
from bokeh.embed import components

palette.reverse() #reverse color palette.

counties = {
    code: county for code, county in counties.items() if county["state"] == "ca"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [county_rate for county_rate in treatment_gap]
color_mapper = LinearColorMapper(palette=palette, low=2000, high=10000)

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
))

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Not enough MDs, too many patients: CA Population Treatment Gap, 2018", tools=TOOLS,
    x_axis_location=None, y_axis_location=None
)
p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Waiting List Size ", "@rate"),
    ("(Long, Lat)", "($x, $y)"),]

# show(p)

#write files for flask.
script4, div4 = components(p)
h1 = open('/Users/erikagutierrez/Desktop/Website/static/graph_4_script.html', 'w')
h1.write(script4)
h2 = open('/Users/erikagutierrez/Desktop/Website/static/graph_4_div.html', 'w')
h2.write(div4)
