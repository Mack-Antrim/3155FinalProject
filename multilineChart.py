import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import config

#authors britt and aiden


class multilineChart:

    global maxAQIdict
    # A function that creates a multiline chart given a particular state
    #@staticmethod
    def multiLineChart(self, state):

        maxAQIdict = {}

        for i in config.years:
            testString = 'https://raw.githubusercontent.com/Mack-Antrim/3155FinalProject/main/AQI_Data/annual_aqi_by_county_xxxx.csv'
            url = testString.replace('xxxx', i)
            # Create a "data" object that is the file
            data = pd.read_csv(url)
            df = pd.DataFrame(data)
            maxAQIdict[i] = {}
            yearsDict = {}
            #year = yearDict
            #inner loop
            for j in config.state_names:

                isState = (df['State'] == j)
                isStatedf = df[isState]
                mean = isStatedf['Max AQI'].mean()
                yearsDict[j] = mean

            maxAQIdict[i] = yearsDict

        #test access of information by printing each Alabama value - successful
        #for i in maxAQIdict:
            #print(maxAQIdict[i]['Alabama'])
#test making a dataframe out of the dictionary
        maxAQIperState = pd.DataFrame.from_dict(
            maxAQIdict,
            orient="index", columns=config.state_names)

        trace1 = go.Scatter(x=config.years,
                            y=maxAQIperState[state],
                            mode='lines',
                            name='Average MAX AQI')

        layout = go.Layout(title=state,
                           xaxis_title="Year",
                           yaxis_title="MAX AQI")

        return {'data': trace1, 'layout': layout}

        #fig = go.Figure(data=trace1, layout=layout)

        #pyo.plot(fig, filename='testMulti.html')
    #def multilinechart(state1, state2, state3):