import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from data import get_datadot


plotly.plotly.sign_in(username='watthell234', api_key='MZVM8WScV46o6NAKGsjY')

## Thinking I need to create objects to build shit like an engineer
app = dash.Dash(__name__)
server = app.server

data = get_datadot()

#table.to_csv('data.csv')
x = data.original_air_year
y = data.total_us_viewers_in_millions

# graph attributes
trace1 = go.Scatter(x = x, y = y,  fill = 'tonexty', line = dict(color = 'rgb(240,230,140)'), name='US Viewers (in millions)')
# dash layout attributes
lay1 = go.Layout(
    autosize=True,
    title= 'Simpsons Viewers by release Year',
    showlegend= True,
    annotations = [dict(x=data.iloc[data['total_us_viewers_in_millions'].idxmax(), 0],
                        y=np.max(y),
                        xref='x',
                        yref='y',
                        text='Peak: {0}M Viewers'.format(int(round(np.max(y),0))),
                        showarrow=True,
                        font=dict(
                family='Courier New, monospace',
                size=16,
                color='#ffffff'
            ),
            align='center',
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#636363',
            ax=40,
            ay=-30,
            bordercolor='#c7c7c7',
            borderwidth=2,
            borderpad=4,
            bgcolor='#636363',
            opacity=0.8)] )


app.layout = html.Div(children=[
    html.H1(children="Simpsons Analysis"),


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
