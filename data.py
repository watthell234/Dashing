import datadotworld as dw
import plotly
import plotly.graph_objs as go
import datetime as dt
import numpy as np
import pandas as pd
import os

config = dw.EnvConfig()


# data retrival
def get_datadot():
    lds = dw.load_dataset('data-society/the-simpsons-by-the-data')
    simpsons_eps = lds.dataframes['simpsons_episodes'].sort_values(by='original_air_date', axis=0, ascending=True)
    simpsons_eps['original_air_date'] = pd.to_datetime(simpsons_eps['original_air_date'])
    simpsons_eps['original_air_year'] = simpsons_eps['original_air_date'].dt.year
    table = simpsons_eps.pivot_table(index='original_air_year', values='us_viewers_in_millions', aggfunc=np.sum).sum(axis=1).reset_index()
    table = pd.DataFrame(table)
    table.columns = ['original_air_year', 'total_us_viewers_in_millions']

    return table

#x = table.original_air_year.tolist()
#y = table.total_us_viewers_in_millions.tolist()
