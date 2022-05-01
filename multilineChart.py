import pandas as pd
import plotly.graph_objs as go
import config
from dash import Dash, dcc, html, Input, Output

class multiLineChart:

    @staticmethod
    def multiline(state) -> object:
        # multiColumnns = ['State', 'MaxAQI']
        maxAQIperState = pd.DataFrame(columns=['year', 'mean'])
        for i in config.years:
            testString = 'https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/AQI_Data/annual_aqi_by_county_xxxx.csv'
            url = testString.replace('xxxx', i)
            # Create a "data" object that is the file
            data = pd.read_csv(url)
            df = pd.DataFrame(data)

            newdf = df[df['State'] == state]
            newdf = newdf.loc[:, newdf.columns.isin(['State', 'Max AQI'])]
            newdf['mean'] = newdf['Max AQI'].mean()
            newdf['year'] = i
            newdf = newdf.loc[:, newdf.columns.isin(['year', 'mean'])].drop_duplicates()
            maxAQIperState = pd.concat([maxAQIperState, newdf])
            # print(newdf)

        trace1 = go.Scatter(x=maxAQIperState['year'],
                            y=maxAQIperState['mean'],
                            mode='lines',
                            name='Average MAX AQI')
        data = [trace1]

        layout = go.Layout(title=state,
                           xaxis_title="Year",
                           yaxis_title="MAX AQI")

        fig = go.Figure(data=data, layout=layout)
        return fig

    @staticmethod
    def displayMulti():
        app = Dash()

        app.layout = html.Div([
            html.H1(children='Python Dash',
                    style={
                        'textAlign': 'center',
                        'color': '#ef3e18'
                    }
                    ),
            html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
            html.Div('Average MAX AQI By State -  1/01/2010 to 12/31/2021', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            dcc.Graph(id='line chart'),
            html.Div('Please select a state', style={'color': '#ef3e18', 'margin': '10px'}),
            dcc.Dropdown(
                id='select-state',
                options=config.state_labels,
                value='New York'
            ),
            html.Br(),
            html.Br(),
            dcc.Link('Go back to Home', href='/'),
            html.Br(),
            dcc.Link('Go to Bar Chart', href='/barChart'),
            html.Br(),
            dcc.Link('Go to Bubble Chart', href='/bubbleChart')
        ])

        return app


