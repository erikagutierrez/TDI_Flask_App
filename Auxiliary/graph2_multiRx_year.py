'''Group counts by drug name by year.'''

import sqlite3

conn = sqlite3.connect('/Users/erikagutierrez/Desktop/DataScience/TDI/TechTest/stateRx.db')
cur = conn.cursor()

qs1 = """SELECT period_covered, product_fda_list_name, sum(number_of_prescriptions)
from `2012_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, sum(number_of_prescriptions)
from `2013_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, sum(number_of_prescriptions)
from `2014_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, sum(number_of_prescriptions)
from `2015_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, sum(number_of_prescriptions)
from `2016_state_drug`
where 1
group by product_fda_list_name

UNION all

select period_covered, product_fda_list_name, sum(number_of_prescriptions)
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

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.embed import components




years = sorted([*d.keys()])
print(years)
# years = ['2012', '2013', '2014', '2015', '2016', '2017']
data = {}
data['years'] = years

for year in years:
    drugs_to_counts = d[year] #maps drug name to amount of drug used in the given year

    for drug, count in drugs_to_counts.items(): #'METHADONE', '54'
        if drug not in data:
            data[drug] = []
        data[drug].append(int(count))

print(data)
# data = {'years' : years,
#         'METHADONE'   : [2, 1, 4, 3, 2, 4],
#         'HEROIN'   : [5, 3, 3, 2, 4, 6],
#         'KRATOM'   : [3, 2, 4, 4, 5, 3]}

palette = ["#3288bd", "#99d594", "#e6f598", "#fee08b", "#fc8d59", "#d53e4f", "#ff0000", "#00ff00", "#0000ff", "#ff00ff"]

# this creates [ ("2012", "drug"), ("2013", "drug"),  ... ]
x = [ (year, drug) for year in years for drug in all_drugs ]
print(x)

counts = sum(zip(*[data[drug] for drug in all_drugs]), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=350, title="US: Diversity in Prescriptions by Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=all_drugs, start=1, end=2))

p.y_range.start = 0
p.yaxis.axis_label = 'Total Number of Prescriptions'
p.x_range.range_padding = 0.025
p.xaxis.major_label_orientation = "vertical"
p.xaxis.major_label_text_font_size = "5pt"
p.xgrid.grid_line_color = None
p.left[0].formatter.use_scientific = False


#show(p)

script2, div2 = components(p)
h1 = open('graph_2_script.html', 'w')
h1.write(script2)
h2 = open('graph_2_div.html', 'w')
h2.write(div2)
