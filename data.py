data.py

# Dependencies and Setup
import pandas as pd
from IPython.display import HTML

# File to Load (Remember to Change These)
file_to_load = "../Resources/cities.csv"

# Read Purchasing File and store into Pandas data frame
cities_data = pd.read_csv(file_to_load)
print(cities_data)

cities_data['City'] = cities_data['City'].str.title()
print(cities_data)

result = cities_data.to_html()
print(result)