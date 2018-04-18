import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import datetime as dt
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
x = data.original_air_year.tolist()
y = data.total_us_viewers_in_millions.tolist()

# graph attributes
trace1 = go.Bar(x = x, y = y, marker=dict(color= ['rgb(240,230,140)', 'rgb(50,0,0)']), name='US Viewers (in millions)')
# dash layout attributes
lay1 = go.Layout(
    title= 'Simpsons Viewers by release Year',
    showlegend= True )


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Thhhhhe Simpsonsss"),


    dcc.Graph(
        id='simpson_viewership_trend',
        config={'displayModeBar': False},
        figure={
            'data': [trace1],

            'layout': lay1
            }
        )

])

if __name__ == '__main__':
    app.run_server(debug=True)
