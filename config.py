# Crucial for overall application
# This file serves as a reference for arrays used in charts and functions


state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
               "District Of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
               "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
               "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
               "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
               "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
               "Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# tempStateNames = []

# for i in state_names:
# tempStateNames.append({'label': i, 'value': i})

state_labels = [{'label': 'Alabama', 'value': 'Alabama'}, {'label': 'Alaska', 'value': 'Alaska'},
                {'label': 'Arizona', 'value': 'Arizona'},
                {'label': 'Arkansas', 'value': 'Arkansas'}, {'label': 'California', 'value': 'California'},
                {'label': 'Colorado', 'value': 'Colorado'}, {'label': 'Connecticut', 'value': 'Connecticut'},
                {'label': 'District Of Columbia', 'value': 'District Of Columbia'},
                {'label': 'Delaware', 'value': 'Delaware'}, {'label': 'Florida', 'value': 'Florida'},
                {'label': 'Georgia', 'value': 'Georgia'}, {'label': 'Hawaii', 'value': 'Hawaii'},
                {'label': 'Idaho', 'value': 'Idaho'}, {'label': 'Illinois', 'value': 'Illinois'},
                {'label': 'Indiana', 'value': 'Indiana'}, {'label': 'Iowa', 'value': 'Iowa'},
                {'label': 'Kansas', 'value': 'Kansas'}, {'label': 'Kentucky', 'value': 'Kentucky'},
                {'label': 'Louisiana', 'value': 'Louisiana'}, {'label': 'Maine', 'value': 'Maine'},
                {'label': 'Maryland', 'value': 'Maryland'}, {'label': 'Massachusetts', 'value': 'Massachusetts'},
                {'label': 'Michigan', 'value': 'Michigan'}, {'label': 'Minnesota', 'value': 'Minnesota'},
                {'label': 'Mississippi', 'value': 'Mississippi'}, {'label': 'Missouri', 'value': 'Missouri'},
                {'label': 'Montana', 'value': 'Montana'}, {'label': 'Nebraska', 'value': 'Nebraska'},
                {'label': 'Nevada', 'value': 'Nevada'}, {'label': 'New Hampshire', 'value': 'New Hampshire'},
                {'label': 'New Jersey', 'value': 'New Jersey'}, {'label': 'New Mexico', 'value': 'New Mexico'},
                {'label': 'New York', 'value': 'New York'}, {'label': 'North Carolina', 'value': 'North Carolina'},
                {'label': 'North Dakota', 'value': 'North Dakota'}, {'label': 'Ohio', 'value': 'Ohio'},
                {'label': 'Oklahoma', 'value': 'Oklahoma'}, {'label': 'Oregon', 'value': 'Oregon'},
                {'label': 'Pennsylvania', 'value': 'Pennsylvania'}, {'label': 'Puerto Rico', 'value': 'Puerto Rico'},
                {'label': 'Rhode Island', 'value': 'Rhode Island'},
                {'label': 'South Carolina', 'value': 'South Carolina'},
                {'label': 'South Dakota', 'value': 'South Dakota'}, {'label': 'Tennessee', 'value': 'Tennessee'},
                {'label': 'Texas', 'value': 'Texas'}, {'label': 'Utah', 'value': 'Utah'},
                {'label': 'Vermont', 'value': 'Vermont'}, {'label': 'Virgin Islands', 'value': 'Virgin Islands'},
                {'label': 'Virginia', 'value': 'Virginia'}, {'label': 'Washington', 'value': 'Washington'},
                {'label': 'West Virginia', 'value': 'West Virginia'}, {'label': 'Wisconsin', 'value': 'Wisconsin'},
                {'label': 'Wyoming', 'value': 'Wyoming'}]
pollutant_list = ['Carbon monoxide', 'Nitrogen dioxide (NO2)', 'Sulfur dioxide', 'PM2.5 Local Conditions']

pollutant_labels = [{'label': 'Carbon Monoxide', 'value': 'CO 8-hour 1971'},
                    {'label': 'Nitrogen Dioxide', 'value': 'NO2 1-hour 2010'},
                    {'label': 'Ozone', 'value': 'Ozone 8-Hour 2008'},
                    {'label': 'PM2.5 Local Conditions', 'value': 'PM25 24-hour 2012'},
                    {'label': 'Sulfur dioxide', 'value': 'SO2 1-hour 2010'}]

pollutant_test = {'Carbon Monoxide': 'CO 8-hour 1971',
                  'Nitrogen Dioxide': 'NO2 1-hour 2010',
                  'Ozone': 'Ozone 8-Hour 2008',
                  'PM2.5 Local Conditions': 'PM25 24-hour 2012',
                  'Sulfur dioxide': 'SO2 1-hour 2010'}
pollutant_color = {'Carbon Monoxide': 'rdbu',
                   'Nitrogen Dioxide': 'Hot',
                   'Ozone': 'thermal',
                   'PM2.5 Local Conditions': 'rainbow',
                   'Sulfur dioxide': 'viridis'}
pol_units = {'Carbon Monoxide': 'Parts Per Million',
             'Nitrogen Dioxide': 'Parts Per Billion',
             'Ozone': 'Parts Per Million',
             'PM2.5 Local Conditions': 'Micrograms/cubic meter (LC)',
             'Sulfur dioxide': 'Parts Per Billion'}
year_labels = [
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
]