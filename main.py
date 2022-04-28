# main file to run charts page

from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import config
import multilineChart as m
import barChart as bC

# initialize dash app
app = Dash(__name__)
runner = m
bRunner = bC


# layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }),
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
    html.Br(),
    html.Div('Average MAX AQI per state per year 2010-2021', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    dcc.Graph(id='bar chart'),
    dcc.Slider(2010, 2021, step=None, marks={
        2010: '2010',
        2011: '2011',
        2012: '2012',
        2013: '2013',
        2014: '2014',
        2015: '2015',
        2016: '2016',
        2017: '2017',
        2018: '2018',
        2019: '2019',
        2020: '2020',
        2021: '2021'
    }, value=2011, id='year_slide'),
    html.Br(),
    html.Br()

])


# line chart callback
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


# bar chart callback
@app.callback(
    Output("bar chart", "figure"),
    [Input("year_slide", "value")])
def update_chart(selected_year):
    _year = str(selected_year)
    return bRunner.barFunction(_year)


if __name__ == '__main__':
    app.run_server()

@app.callback(
    Output("bar chart", "figure"),
    [Input("year_slide", "value")])
def update_chart(selected_year):
    _year = str(selected_year)
    return bRunner.barFunction(_year)


if __name__ == '__main__':
    app.run_server()
