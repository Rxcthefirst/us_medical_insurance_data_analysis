#  Project from Codecademy involving analysis of U.S. Medical Insurance Data
#  Collaboration with DenisLazuk and Olubunmi-Amoke

# -----------------------------------------------------------

#  Using pandas to read in the data frame.
import pandas as pd
# -----------------------------------------------------------


#  Read in dataframe from csv file and print header to inspect data.
df = pd.read_csv('insurance.csv')
#print(df.head())

# -----------------------------------------------------------
#  Creating a separate dataframe demonstrating how to filter values from a category.
females = df[df.sex=='female']
print(females)

