import pandas as pd
import config
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


class bubbleUS:
    # def __init__(self, pollutant, year):
    # self.pollutant = pollutant
    # self.year = year

    def USMapFunction(self, pollutant, year) -> object:
        testString = 'https://media.githubusercontent.com/media/Mack-Antrim/3155FinalProject/master/Downloads/3155FinalAnnualConcDataSets/annual_conc_by_monitor_xxxx.csv'
        #testString = 'MonitorData/annual_conc_by_monitor_xxxx.csv'
        url = testString.replace('xxxx', year)

        _pollutant = config.pollutant_test.get(pollutant)

        df = pd.read_csv(url)

        # create new dataframe filtered with chosen pollutant
        new_df = df[df['Pollutant Standard'] == _pollutant]

        # if there is no CBSA name, instead display the County Name and state
        new_df['text'] = new_df['County Name'] + ' County, ' + new_df['State Name']
        new_df['CBSA Name'].fillna(new_df['text'], inplace=True)

        # filter new_df down to the required columns
        columns = ['CBSA Name', 'Arithmetic Mean', 'Latitude', 'Longitude']
        new_df = new_df.loc[:, new_df.columns.isin(columns)]
        new_df = new_df.sort_values(by=['Arithmetic Mean'], ascending=False)

        # determine z-scores for bubble scaling and drop significant outliers
        mean = new_df['Arithmetic Mean'].mean()
        stdev = new_df['Arithmetic Mean'].std()
        new_df['z-score'] = ((new_df['Arithmetic Mean'] - mean) / stdev)
        new_df = new_df[new_df['z-score'] < 5]

        # set negative values to zero to properly display graph
        new_df['Arithmetic Mean'] = new_df['Arithmetic Mean'].apply(lambda x: x if x > 0 else 0)

        # reset indices
        new_df = new_df.reset_index(drop=True)

        sdf = new_df
        fig = px.scatter_geo(sdf, scope='usa', locationmode='USA-states', lon=sdf['Longitude'],
                             lat=sdf['Latitude'], color="Arithmetic Mean",
                             color_continuous_scale=config.pollutant_color.get(pollutant),
                             hover_name="CBSA Name", size='Arithmetic Mean', opacity=.75
                             )
        fig.update_layout(
            title_text=year + ' US ' + pollutant + ' levels<br>' + 'Standard: ' + _pollutant + '<br>Units of Measurement: ' + config.pol_units.get(
                pollutant),
            showlegend=True,
            geo=dict(
                scope='usa',
                landcolor='rgb(217, 217, 217)',
            ),
            height=1000
        )
        # fig.show()
        return fig

    # A function that creates a barchart with a dropdown menu to select a year
    def interactiveBubble(self):
        app = Dash()

        app.layout = html.Div([
            html.H1("Max AQI by State"),
            dcc.RadioItems(
                options=[
                    {'label': 'Carbon Monoxide', 'value': 'Carbon Monoxide'},
                    {'label': 'Nitrogen Dioxide', 'value': 'Nitrogen Dioxide'},
                    {'label': 'Ozone', 'value': 'Ozone'},
                    {'label': 'PM 2.5', 'value': 'PM2.5 Local Conditions'},
                    {'label': 'Sulfur dioxide', 'value': 'Sulfur dioxide'}],
                value='Ozone',
                inline=True,
                id='radio'
            ),
            dcc.Graph(id="graph"),
            dcc.Dropdown(
                id="select-year",
                options=config.year_labels,
                value="2010"
            )
        ])

        @app.callback(
            Output("graph", "figure"),
            Input('radio', 'value'),
            Input("select-year", 'value')
        )
        def update_chart(radio_name, year_name):
            return self.USMapFunction(radio_name, year_name)

        app.run_server(debug=True)


#b = bubbleUS()
#b.interactiveBubble()
