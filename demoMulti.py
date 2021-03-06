# Author: Britt Field
# version 1.31
# file to test dash app creation with the multiline chart function

from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import config
import multilineChart as m

#initialize dash app
app = Dash(__name__)
runner = m

# layout
app.layout = html.Div(children=[
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
    html.Div('Please select up to three states', style={'color': '#ef3e18', 'margin': '10px'}),
    dcc.Dropdown(
        id='select-state',
        options=config.state_labels,
        value='New York'
    ),
    html.Br(),
    html.Br()

])


@app.callback(Output('line chart', 'figure'),
              [Input('select-state', 'value')])
def update_figure(selected_state):
    _state = selected_state
    graphGuts = runner.multilineChart(_state)
    return graphGuts


if __name__ == '__main__':
    app.run_server(debug=True)


@app.callback(Output('line chart', 'figure'),
              [Input('select-state', 'value')])
def update_figure(selected_state):
    _state = selected_state
    graphGuts = runner.multilineChart(_state)
    return graphGuts


if __name__ == '__main__':
    app.run_server()
