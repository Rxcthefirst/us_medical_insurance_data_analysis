#  Project from Codecademy involving analysis of U.S. Medical Insurance Data
#  Collaboration with DenisLazuk and Olubunmi-Amoke

# -----------------------------------------------------------

#  Using pandas to read in the data frame.
import pandas as pd
# -----------------------------------------------------------


#  Read in dataset from csv file and create dataframe. Print header to inspect data.
df = pd.read_csv('insurance.csv')
print(df)

# -----------------------------------------------------------
#  Creating a separate dataframe demonstrating how to filter values from a category.
females = df[df.sex=='female']


# -----------------------------------------------------------
#  Filter original dataframe for people who have at least one child
one_child_plus = df[df.children>0]
print(one_child_plus)

# -----------------------------------------------------------
#  Average age of the data points with at least one child
number_of_data_points = len(one_child_plus)
print(sum(one_child_plus['age'])/number_of_data_points)



