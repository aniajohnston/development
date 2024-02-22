# api pulls data from survey software
# the data gotten is called response.json 
# pandas is similar this library will create a data frame from the json
# we will get a list from this 

import pandas as pd

animals = ['Lions', 'Tigers', 'Bears', 'Dogs', 'Cats' ] #List collection

df = pd.DataFrame(animals) #Convert our list to a format which Pandas can use

# print(df)

df.to_csv('output.csv') #this will give us our output