
# data module to import into every module we want to access lists


state_names = [ "Alabama","Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "District Of Columbia", "Delaware", "Florida", "Georgia",  "Hawaii", "Idaho", "Illinois", "Indiana","Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota","Mississippi", "Missouri", "Montana",  "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota","Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah","Vermont", "Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

tempStateNames = []

for i in state_names:
    tempStateNames.append({'label': i, 'value': i})

state_labels = tempStateNames