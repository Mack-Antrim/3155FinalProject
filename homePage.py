from dash import dcc
from dash import html
from dash import Dash

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
            }),
    html.Br(),
    html.Br(),
    html.Table(className='memberTable',
               children=[
                html.Tr([html.Th('Group Members'), html.Th('Contact')]),]
               + [
                   html.Tr([html.Td('Dexter Osha'), html.Td('oink')]),
                   html.Tr([html.Td('Mack Antrim'), html.Td('oink')]),
                   html.Tr([html.Td('Britt Fields'), html.Td('oink')]),
                   html.Tr([html.Td('Jaimik Dholiya'), html.Td('oink')]),
                   html.Tr([html.Td('Aidan Hanger'), html.Td('oink')])
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
                html.Tr([html.Th('Charts'), html.Th('Link')])
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
    html.H2(children= html.I(disclaimer),
            style={
                'textAlign': 'center',
                'color': 'ef3e18',
                'fontSize': 25,
                'fontStyle': 'italics',
                'width': '50%',
                'marginLeft': 'auto',
                'marginRight': 'auto',
            })

])



if __name__ == '__main__':
    app.run_server(debug=True)