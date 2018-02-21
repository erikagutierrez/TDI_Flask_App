'''Group counts by drug name by year.'''

import sqlite3

conn = sqlite3.connect('/Users/erikagutierrez/Desktop/DataScience/TDI/TechTest/stateRx.db')
cur = conn.cursor()

qs1 = """SELECT period_covered, product_fda_list_name, count(1)
from `2012_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, count(1)
from `2013_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, count(1)
from `2014_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, count(1)
from `2015_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, count(1)
from `2016_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, count(1)
from `2017_state_drug`
where 1
group by product_fda_list_name"""

all_rows = cur.execute(qs1)

'''make dictionary of dictionaries to organize data'''

all_drugs = "buprenorphine,butrans,zubsolv,naloxone,methadone,suboxone,bunavail,buprenex,probuphine,subutex".upper().split(',')

d = dict()

for row in all_rows :
    year = row[0]
    drug = row[1]
    amount = row[2]
    if year not in d :
        d[year] = {}
        for i in all_drugs:
            d[year][i] = 0

    d[year][drug] = amount


'''plot the data in bokeh: grouped by medication type'''

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure

output_file("bar_stacked_multiRx.html")

years = sorted([*d.keys()])
# years = ['2012', '2013', '2014', '2015', '2016', '2017']

data = {}
data['years'] = years

for year in years:
    drugs_to_counts = d[year] #maps drug name to amount of drug used in the given year

    for drug, count in drugs_to_counts.items(): #'METHADONE', '54'
        if drug not in data:
            data[drug] = []
        data[drug].append(int(count))

# data = {'years' : years,
#         'METHADONE'   : [2, 1, 4, 3, 2, 4],
# etc

# this creates [ ("2012", "drug"), ("2013", "drug"),  ... ]
# x = [ (year, drug) for year in years for drug in all_drugs ]
# # print(x)
# counts = sum(zip(*[data[drug] for drug in all_drugs]), ()) 
# source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(y_range=all_drugs, plot_height=350, x_range=(0, 4000), title="Rx: Number per Year",
           toolbar_location=None)

p.hbar_stack(years, y='all_drugs', height=0.9, color=GnBu3, source=ColumnDataSource(data),
             legend=["%s exports" % x for x in years])

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

show(p)
