import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import config
import numpy as np


class bubbleUS:
    def __init__(self, pollutant, year):
        self.pollutant = pollutant
        self.year = year


def USMapFunction(pollutant, year) -> object:
    # testString = 'https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/AQI_Data/annual_aqi_by_county_xxxx.csv'
    testString = 'MonitorData/annual_conc_by_monitor_2020.csv'
    url = testString.replace('xxxx', year)

    _pollutant = config.pollutant_test.get(pollutant)

    df = pd.read_csv(url)

    # create new dataframe filtered with chosen pollutant
    new_df = df[df['Pollutant Standard'] == _pollutant]

    limits = [(0.001, 0.002), (0.002, 0.003), (0.00301, 0.0032), (0.0033, 0.0036), (0.00361, 0.00365), (0.00366, 1)]
    colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey", "yellow"]
    scale = 5000

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = new_df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=df_sub['Longitude'],
            lat=df_sub['Latitude'],
            text=df_sub['CBSA Name'],
            marker=dict(
                size=df_sub['Arithmetic Mean'],  # / scale,
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            ),
            name='{0} - {1}'.format(lim[0], lim[1])))
    fig.update_layout(
        title_text='2014 US city populations<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        )
    )

    fig.show()


b = bubbleUS
USMapFunction('Ozone', '2020')