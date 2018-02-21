from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components

import sqlite3

conn = sqlite3.connect('/Users/erikagutierrez/Desktop/DataScience/TDI/TechTest/stateRx.db')
cur = conn.cursor()

'''The following sql query was conducted:'''
qs1 = """SELECT period_covered, sum(number_of_prescriptions)
	FROM `2012_state_drug`

union all

SELECT period_covered, sum(number_of_prescriptions)
	FROM `2013_state_drug`

union all

SELECT period_covered, sum(number_of_prescriptions)
	FROM `2014_state_drug`

union all

SELECT period_covered, sum(number_of_prescriptions)
	FROM `2015_state_drug`

union all

SELECT period_covered, sum(number_of_prescriptions)
	FROM `2016_state_drug`

union all

SELECT period_covered, sum(number_of_prescriptions)
	FROM `2017_state_drug`"""

all_rows = cur.execute(qs1) #<class 'sqlite3.Cursor'>
#row = cur.fetchone() #this is the first row.
years = list()
counts = list()
for row in all_rows :
    year = row[0]
    num_rx = row[1]
    years.append(year)
    counts.append(num_rx)



source = ColumnDataSource(data=dict(years=years, counts=counts))

p = figure(x_range=years, plot_height=350, toolbar_location=None, title="US: Number of Rx Prescribed per Year")
p.vbar(x='years', top='counts', width=0.9, source=source, legend="years",
       line_color='white', fill_color=factor_cmap('years', palette=Spectral6, factors=years))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 2500000
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
p.left[0].formatter.use_scientific = False

#show(p)

script1, div1 = components(p)
h1 = open('graph_1_script.html', 'w')
h1.write(script1)
h2 = open('graph_1_div.html', 'w')
h2.write(div1)
