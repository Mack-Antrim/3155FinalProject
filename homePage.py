# Author: Dexter Osha
# This file creates the splash page for the overall application
# Has contact information for eac member as well as links to the charts in use
from dash import dcc
from dash import html
from dash import Dash

@staticmethod
def homePage():
    app = Dash(__name__)

    landingQuote = "Welcome to the landing page of Team Twenty's interactive python dash application explaining the different types of pollutants in the air " \
                   "and showing the changes of air quality throughout the United States within the past 12 years, We are conveying this information through graphical visualization that will allow " \
                   "for inferences to be made on the major impact to the global climate with changes in lifestyle and industry"
    disclaimer = "Please keep in mind that some loading times may vary because of the size of the datasets we are using. However, You will still be able to view the graphs"

    members = "Dexter Osha, Mack Antrim, Britt Fields, Jaimik Dholyia, Aiden Hanger"


    app.layout = html.Div(children=[

        html.H1(children=landingQuote,
                style={
                    'textAlign': 'center',
                    'color': 'ef3e18',
                    'fontSize': 25,
                    'width': '50%',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',

                }),
        html.Br(),
        html.Br(),
        html.H1(dcc.Link('Start Here', href='/infoTable'),
                style={
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'center'
                }),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Table(className='graphTable',
                   children=[
                    html.Tr( html.Th('Visuals'))
                   ] + [
                    html.Tr([html.Td(dcc.Link("Visualize each state's AQI over the course of one year between 2010 and 2021 using a bar chart", href='/barChart'))]),
                    html.Tr(),
                    html.Tr(),
                    html.Tr([html.Td(dcc.Link('Individually visualize the different concentrations of the five main air pollutants throughout the course of a year within the United States using a bubble-map', href='/bubbleChart'))]),
                    html.Tr(),
                    html.Tr(),
                    html.Tr([html.Td(dcc.Link("Visualize each state's max AQI from the years 2010 - 2021 using a line chart", href='/multiLine'))]),

                   ],
                   style={
                       'border': 'thick solid black',
                       'text-align': 'Center',
                       'color': 'ef3e18',
                       'fontSize': 23,
                       'width': 600,
                       'height': 325,
                       'marginLeft': 'auto',
                       'marginRight': 'auto'
                   }),

        html.Br(),
        html.Br(),
        html.H2(children=html.I(disclaimer),
                style={
                    'textAlign': 'center',
                    'color': 'ef3e18',
                    'fontSize': 25,
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                }),
        html.Br(),
        html.Br(),
        html.Table(className='sources',
                   children=[
                       html.Tr([html.Th('Source Of Data (opens in new tab)')])
                       ] + [
                       html.Tr([html.Td(html.A("EPA Website Data-Sets", href='https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual', target="_blank"))])
                   ],
                   style={
                       'border': 'thick solid black',
                       'text-align': 'center',
                       'fontsize': 23,
                       'width': 600,
                       'marginLeft': 'auto',
                       'marginRight': 'auto'
                   }),
        html.Br(),
        html.Br(),

        html.Footer(children=members,
                    style={
                        'text-align': 'center'
                    })


    ])
    return app



