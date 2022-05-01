# main file to run charts page

from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
from barChart import barChart
from infoTable import infoTable
from multilineChart import multiLineChart as m
from bubbleChart import bubbleUS
from homePage import homePage

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# The Landing page layout
index_page = homePage().layout

# info table page
info_page = infoTable().layout

#The Bar Chart layout and dropdown menu
#barChart_layout = barChart.interactiveBarChart().layout

@callback(Output("graph", "figure"),
     [Input("select-year", "value")])
def update_chart(year):
    return barChart.barFunction(year)

# The multi-line chart and dropdown menu
multiLine_layout = m.displayMulti().layout

@app.callback(
            Output("line chart", "figure"),
            [Input("select-state", "value")])
def update_chart(_state):
    return m.multiline(_state)

# The bubble chart and options
bubbleChart_layout = bubbleUS.interactiveBubble().layout

@app.callback(
            Output("bubble", "figure"),
            Input('radio', 'value'),
            Input("select-time", 'value')
        )
def update_chart(radio_name, year_name):
     return bubbleUS.USMapFunction(radio_name, year_name)

@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/barChart':
        return barChart_layout
    elif pathname == '/multiLine':
        return multiLine_layout
    elif pathname == '/bubbleChart':
        return bubbleChart_layout
    elif pathname == '/infoTable':
        return info_page
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True)

