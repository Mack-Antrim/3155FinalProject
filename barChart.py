from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objs as go
import config


class barChart:

    # A function that generates a barchart given a year.
    @staticmethod
    def barFunction(year):
        testString = 'https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/AQI_Data/annual_aqi_by_county_xxxx.csv'
        url = testString.replace('xxxx', year)
        # Create a "data" object that is the file
        data = pd.read_csv(url)

        # Create a data frame  object or "df" using the         "data"   file
        df = pd.DataFrame(data)

        maxAQIdict = {'State': [], 'MAX AQI': []}

        for i in config.state_names:
            isState = (df['State'] == i)  # T/F return on whether or not the state name is in the dateframe
            isStatedf = df[isState]  # create a new dataframe with all of the confirmed states
            mean = isStatedf[
                'Max AQI'].mean()  # variable to hold the mean for all of the Max AQI readings for individual state
            maxAQIdict['State'].append(i)
            maxAQIdict['MAX AQI'].append(mean)

        # generate new dataset with all states and their Average MAX AQI
        aqiDF = pd.DataFrame(maxAQIdict)
        # Bar Chart test
        data = [go.Bar(x=aqiDF['State'], y=aqiDF['MAX AQI'])]

        xTitleTemp = 'Average Maximum AQI by State for xxxx'
        xTitle = xTitleTemp.replace('xxxx', year)
        layout = go.Layout(title=xTitle, xaxis_title='States', yaxis_title='AQI Index')

        # plot the figure to HTML file
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(color_continuous_scale=[(0.00, "Green"), (50.0, 'Green'), (51.0, 'Yellow'), (100.0, 'Yellow'), (101.0, 'Orange'), (150, 'Orange'), (151, 'Red'), (200, 'Red'), (201, 'Purple'), (300, 'Purple'), (301, 'Black'), (500, 'Black')],
                          coloraxis_colorbar = dict(
                              title = 'AQI Ratings',
                              tickvals = [1, 2, 3, 4, 5],
                              ticktext = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
                          ))
        return fig


    # A function that creates a barchart with a dropdown menu to select a year
    @staticmethod
    def interactiveBarChart():

        app = Dash()
        app.layout = html.Div([
            html.H1("Max AQI by State"),
            dcc.Dropdown(
                id="select-year",
                options=[
                    {'label': '2010', 'value': '2010'},
                    {'label': '2011', 'value': '2011'},
                    {'label': '2012', 'value': '2012'},
                    {'label': '2013', 'value': '2013'},
                    {'label': '2014', 'value': '2014'},
                    {'label': '2015', 'value': '2015'},
                    {'label': '2016', 'value': '2016'},
                    {'label': '2017', 'value': '2017'},
                    {'label': '2018', 'value': '2018'},
                    {'label': '2019', 'value': '2019'},
                    {'label': '2020', 'value': '2020'},
                    {'label': '2021', 'value': '2021'}
                ],
                value="2010"
            ),
            dcc.Graph(id="graph"),
            html.Br(),
            dcc.Link('Go back to Home', href='/'),
            html.Br(),
            dcc.Link('Go to Multi-Line Chart', href='/multiLine'),
            html.Br(),
            dcc.Link('Go to Bubble Chart', href='/bubbleChart'),
            html.Br(),
            dcc.Link('Go to Info Table', href='/infoTable')
        ])

        return app