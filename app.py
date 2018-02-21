from flask import Flask, render_template, url_for, request
from data import Articles
from bokeh.embed import components
#graph1
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

# import sqlite3

app = Flask(__name__)
app.debug = True #this allows you to be able to refresh as you build the site rather than reloading each time.

Articles = Articles()

@app.route('/') #create route for website.
def home() :
    return render_template('home.html') #render template called home.html.

@app.route('/rationale')
def rationale() :
    return render_template('rationale.html')

@app.route('/data')
def data() :
    return render_template('data.html')

@app.route('/articles')
def articles() :
    return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>')
def get_article(id) :
    return render_template('get_article.html', id = id)

@app.route('/analysis')
def analysis() :
    # Embed plot into HTML via Flask Render
    # graph 1: Total Number Rx vs. Year
    script_years = open('static/graph_1_script.html', 'r').read()
    div_years = open('static/graph_1_div.html', 'r').read()
    #graph 2: Diversity in Rx by year
    script_multiRx = open('static/graph_2_script.html', 'r').read()
    div_multiRx = open('static/graph_2_div.html', 'r').read()
    #graph 3: CA Medicaid Population OUD Prevalence
    script_caPrev = open('static/graph_3_script.html', 'r').read()
    div_caPrev = open('static/graph_3_div.html', 'r').read()
    #graph 4: CA Medicaid Population OUD Treatment Gap
    script_caTG = open('static/graph_4_script.html', 'r').read()
    div_caTG = open('static/graph_4_div.html', 'r').read()
    #final graph: bubbles, year, Price per Rx, by state
    script_bubbles = open('static/graph_bubbles_script.html', 'r').read()
    div_bubbles = open('static/graph_bubbles_div.html', 'r').read()
    return render_template('analysis.html', script1=script_years, div1=div_years, script2=script_multiRx, div2=div_multiRx, script3=script_caPrev, div3=div_caPrev, script4=script_caTG, div4=div_caTG, script5=script_bubbles, div5=div_bubbles)

@app.route('/Figure1')
def Figure1() :
    return render_template('Figure1.html')

@app.route('/executive_summary')
def executive_summary() :
    return render_template('executive_summary.html')

if __name__ == '__main__' :
    app.run() #should allow us to run application.


#app.run(debug=True) another way to put app in debut mode.
