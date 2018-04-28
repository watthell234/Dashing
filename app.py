import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd


plotly.plotly.sign_in(username='watthell234', api_key='MZVM8WScV46o6NAKGsjY')


app = dash.Dash(__name__)
server = app.server

data = pd.read_csv('data.csv')
#table.to_csv('data.csv')
x = data.original_air_year.tolist()
y = data.total_us_viewers_in_millions.tolist()

# graph attributes
trace1 = go.Bar(x = x, y = y, marker=dict(color= 'rgb(240,230,140)'), name='US Viewers (in millions)')
# dash layout attributes
lay1 = go.Layout(
    autosize=True,
    title= 'Simpsons Viewers by release Year',
    showlegend= True,
    annotations = [dict(x=1990,
                        y=np.max(y),
                        xref='x',
                        yref='y',
                        text='Popularity peaks at 577M Viewers',
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
    html.H1(children="Thhhhheee Simpsonss"),


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
