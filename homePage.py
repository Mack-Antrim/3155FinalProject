# Author: Dexter Osha
from dash import dcc
from dash import html
from dash import Dash

@staticmethod
def homePage():
    app = Dash(__name__)

    landingQuote = "Welcome to the landing page of Team Twenty's interactive python dash showing the changes of air quality throughout the United States throughout the past 12 years, \n" \
                   " we are conveying this information through graphical visualization that will lead inference to the the major impact that can be made on the global climate with minor changes in lifestyle "
    disclaimer = "Please keep in mind that some loading times may vary because of the size of the datasets we are using. However, You will still be able to view the graphs"


    app.layout = html.Div(children=[

        html.H1(children= landingQuote,
                style={
                    'textAlign': 'center',
                    'color': 'ef3e18',
                    'fontSize': 25,
                    'width': '50%',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'border': 'thick solid black'
                }),
        html.Br(),
        html.Br(),
        html.Table(className='memberTable',
                   children=[
                    html.Tr([html.Th('Group Members'), html.Th('Contact')]),]
                   + [
                       html.Tr([html.Td('Dexter Osha'), html.Td(html.A("Github", href='https://github.com/Dexter-Osha', target="_blank")), html.Td(html.A("Linkdin", href='https://www.linkedin.com/in/dexter-osha-209380207/', target="_blank"))]),
                       html.Tr([html.Td('Mack Antrim'), html.Td(html.A("Github", href='https://github.com/Mack-Antrim', target="_blank"))]),
                       html.Tr([html.Td('Britt Fields'), html.Td(html.A("Github", href='https://github.com/bfield-uncc', target="_blank"))]),
                       html.Tr([html.Td('Jaimik Dholiya'), html.Td(html.A("Github", href='https://github.com/Dexter-Osha', target="_blank"))]),
                       html.Tr([html.Td('Aidan Hanger'), html.Td(html.A("Github", href='https://github.com/ahanger246', target="_blank"))])
                   ],
                   style={
                       'border': 'thick solid black',
                       'text-align': 'left',
                       'color': 'ef3e18',
                       'fontSize': 23,
                       'width': 600,
                       'marginLeft': 'auto',
                       'marginRight': 'auto',

                   }),

        html.Br(),
        html.Br(),
        html.Br(),

        html.Table(className='graphTable',
                   children=[
                    html.Tr([html.Th('Charts'), html.Th('Visuals')])
                   ] + [
                    html.Tr([html.Td('Bar Chart'), html.Td(dcc.Link('Bar Chart', href='/barChart'))]),
                    html.Tr([html.Td('Bubble Chart'), html.Td(dcc.Link('Bubble Chart', href='/bubbleChart'))]),
                    html.Tr([html.Td('Line Chart'), html.Td(dcc.Link('Multi-Line Chart', href='/bubbleUS'))]),
                    html.Tr([html.Td('Toxin Info Table'), html.Td(dcc.Link('Toxin Info Table', href='/infoTable'))]),
                   ],
                   style={
                       'border': 'thick solid black',
                       'text-align': 'left',
                       'color': 'ef3e18',
                       'fontSize': 23,
                       'width': 600,
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
                    'border': 'thick solid black',
                    'width': '50%',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                })


    ])
    return app



