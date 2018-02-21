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

ls_county = list()
ls_total_pop = list()

for tup in all_rows :
    ls_county.append(tup[0])
    ls_total_pop.append(tup[1])

#create list of opioid pop in each county. 1% is standard estimate.

ls_opioid_pop = list()
for i in ls_total_pop:
    i = round(i * .02) #multiply by .4 b/c of medicaid pop. adjustment. = total opioid dependent medicaid pop.
    # i = "{:,}".format(i)
    ls_opioid_pop.append(i)
print(ls_opioid_pop)

'''heat map'''
from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.embed import components

palette.reverse()

counties = {
    code: county for code, county in counties.items() if county["state"] == "ca"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [county_rate for county_rate in ls_opioid_pop]
color_mapper = LogColorMapper(palette=palette)

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
))

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="California Estimated Opioid Dependent Population, 2016", tools=TOOLS,
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
    ("Number of OUD Patients ", "@rate"),
    ("(Long, Lat)", "($x, $y)"),
]

# show(p)

#write files for flask.
script3, div3 = components(p)
h1 = open('/Users/erikagutierrez/Desktop/Website/static/graph_3_script.html', 'w')
h1.write(script3)
h2 = open('/Users/erikagutierrez/Desktop/Website/static/graph_3_div.html', 'w')
h2.write(div3)
