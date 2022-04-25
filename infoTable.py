import base64

from dash import Dash, dash_table, html
from dash.dependencies import Input, Output
import pandas as pd



df = pd.read_csv("https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/Pollutant%20Table%20-%20Sheet1%20(6).csv")

app = Dash(__name__)

aqiData = """
Think of the AQI as a yardstick that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality.
For each pollutant an AQI value of 100 generally corresponds to an ambient air concentration that equals the level of the short-term national ambient air quality standard for protection of public health. AQI values at or below 100 are generally thought of as satisfactory. When AQI values are above 100, air quality is unhealthy: at first for certain sensitive groups of people, then for everyone as AQI values get higher.
The AQI is divided into six categories. Each category corresponds to a different level of health concern. Each category also has a specific color. The color makes it easy for people to quickly determine whether air quality is reaching unhealthy levels in their communities.
"""

app.layout = html.Div(children=[
    html.H1(children='AQI Information and Pollutant Information Chart',
            style={'textAlign' : 'center',
                   'color' : 'ef3e18'}
            ),
    html.Br(),
    html.Br(),
    html.H3('How does the AQI Work?', style={'color': '#df1e56'}),
    html.Div(children = aqiData),
    html.Br(),
    html.Img(src= 'https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/Pictures/image1.png'),
    html.Br(),
    html.Br(),
    html.Table(className='airTable', children=
        [html.Tr([html.Th(col) for col in df.columns], style={'fontSize': 22})] +
        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min(len(df), 5))]
            ),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)




"""""
app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_cell={'textAlign': 'left'},
    style_cell_conditional=
    [
        {
            'if': {'column_id': 'Region'},
            'textAlign': 'left'
        }
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
"""
