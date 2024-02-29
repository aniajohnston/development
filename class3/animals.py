# api pulls data from survey software
# the data gotten is called response.json 
# pandas is similar this library will create a data frame from the json
# we will get a list from this 

# pandas is a library
# someone did the code so that you can export to a csv.

import pandas as pd

animals = ['Lions', 'Tigers', 'Bears', 'Dogs', 'Cats' ] #List collection
#brackets are used in python to indicate a list.

df = pd.DataFrame(animals) #Convert our list to a format which Pandas can use
# df means data frame. as pd lets you just shorten the name from pandas to pd
#dataframe a bunch of columns.
#this is a method they come after the .
#parenthesis hold your argument.

# print(df)

df.to_csv('output.csv') #this will give us our output
