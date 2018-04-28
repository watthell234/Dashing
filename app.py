import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from datadotworld.datadotworld import DataDotWorld
from datadotworld.config import EnvConfig

plotly.plotly.sign_in(username='watthell234', api_key='MZVM8WScV46o6NAKGsjY')

dw = DataDotWorld(config=EnvConfig())

app = dash.Dash(__name__)
server = app.server

#data = pd.read_csv('data.csv')
lds = dw.load_dataset('data-society/the-simpsons-by-the-data')
simpsons_eps = lds.dataframes['simpsons_episodes'].sort_values(by='original_air_date', axis=0, ascending=True)
simpsons_eps['original_air_date'] = pd.to_datetime(simpsons_eps['original_air_date'])
simpsons_eps['original_air_year'] = simpsons_eps['original_air_date'].dt.year
table = simpsons_eps.pivot_table(index='original_air_year', values='us_viewers_in_millions', aggfunc=np.sum).sum(axis=1).reset_index()
table = pd.DataFrame(table)
table.columns = ['original_air_year', 'total_us_viewers_in_millions']
#table.to_csv('data.csv')
x = table.original_air_year.tolist()
y = table.total_us_viewers_in_millions.tolist()

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
            ax=20,
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
