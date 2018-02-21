import pandas as pd

from bokeh.core.properties import field
from bokeh.layouts import layout, widgetbox
from bokeh.models import (
    ColumnDataSource, HoverTool, SingleIntervalTicker, CategoricalTicker, Label,
    CategoricalColorMapper
)
from bokeh.models import Legend
from bokeh.palettes import viridis, inferno
from bokeh.plotting import Figure
from bokeh.io import show
from bokeh.embed import components


from gapminder_data import process_data

population_size, state_list = process_data()

df = pd.read_csv('state_methadone_suboxone_restored.csv')


# data cleanup
df['Total Amount Reimbursed'] = df['Total Amount Reimbursed'].astype('float')
df['Total Number of Prescriptions'] = df['Total Number of Prescriptions'].astype('float')

df['Price per Rx'] = df['Price per Rx'].astype('float').round(2).astype('str')
df = df[df['State']!= 'XX']

df['population_size'] = population_size

def morph(series):
     if series.loc['Year'] == 2017:
             series2 = series.copy()
             series2['Total Amount Reimbursed'] = series2['Total Amount Reimbursed'] * 2
             series2['Total Number of Prescriptions'] = series2['Total Number of Prescriptions'] * 2
             return series2
     else:
             return series

df = df.apply(morph, axis = 1)


suboxone_df = df[df['Prescription']== 'Suboxone']
methadone_df = df[df['Prescription']== 'Methadone']

years = [2012,2013,2014,2015,2016,2017]



def plot_suboxone():
    source1 = ColumnDataSource(suboxone_df)
    source2 = ColumnDataSource(methadone_df)

    plot = Figure(x_range=(0,500), y_range=(2011,2018), title='Methadone and Suboxone Pricing Data', plot_height=600, plot_width=1200)
    plot.xaxis.ticker = SingleIntervalTicker(interval=100)
    plot.xaxis.axis_label = "Price per Prescription"
    plot.yaxis.ticker = SingleIntervalTicker(interval = 1)
    plot.yaxis.axis_label = "Year"

    label = Label(x=1.1, y=18, text=str(years[0]), text_font_size='70pt', text_color='#eeeeee')
    plot.add_layout(label)

    color_mapper2 = CategoricalColorMapper(palette=inferno(52), factors=state_list)
    color_mapper1 = CategoricalColorMapper(palette=viridis(52), factors=state_list)

    plot.circle(
        x='Price per Rx',
        y='Year',
        size='population_size',
        source=source1,
        fill_color={'field': 'State', 'transform': color_mapper1},
        fill_alpha=0.8,
        line_color='#7c7e71',
        line_width=0.5,
        line_alpha=0.5,
        # legend=field('State'),
    )
    plot.circle(
        x='Price per Rx',
        y='Year',
        size='population_size',
        source=source2,
        fill_color={'field': 'State', 'transform': color_mapper2},
        fill_alpha=0.8,
        line_color='#7c7e71',
        line_width=0.5,
        line_alpha=0.5,
        # legend=field('State'),
    )
    plot.add_tools(HoverTool(tooltips=[('State ', "@State"), ('Price ', '$@{Price per Rx}'), ('Rx ', '@Prescription'), ('# Rx ', '@{Total Number of Prescriptions}')], show_arrow=False, point_policy='follow_mouse'))
    return(plot)

# show(plot_suboxone())

#write files for flask.
script5, div5 = components(plot_suboxone())
h1 = open('/Users/erikagutierrez/Desktop/Website/static/graph_bubbles_script.html', 'w')
h1.write(script5)
h2 = open('/Users/erikagutierrez/Desktop/Website/static/graph_bubbles_div.html', 'w')
h2.write(div5)
