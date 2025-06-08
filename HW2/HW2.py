import numpy as np
import pandas as pd

#---Q1
# Given the two arrays
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Using np.intersect1d to find the distinct common elements 
unique_items = np.intersect1d(a, b)

# Print the result
print("Common Elements:")
print(unique_items, end="\n\n")



#---Q2
# Create a sequence of numbers from 1 to 15 (inclusive)
# np.arange(start, stop)
sequence = np.arange(1, 16)

# Reshape into a 5x3 array.
# By default, reshape fills row by row ( 1  2  3).
# To fill column by column as per your example, we use 'order='F'' (for Fortran-style order).
result_array = sequence.reshape((5, 3), order='F')

# Print the resulting array
print("5x3 Array:")
print(result_array, end="\n\n")


#---Q3
# Transform result_array into a unidimensional array (flattening)
# We use order='F' agin to do (column-major) order
unidimensional_array = result_array.flatten(order='F')

# Print the flattened array
print("Unidimensional Array:")
print(unidimensional_array, end="\n\n")


#---Q4
# Reshape unidimensional_array into a 3-dimensional array
# use reshape into 3 col with 5 rows with 1 element each
into_3d_array = unidimensional_array.reshape((3, 5, 1))

print("3D Array:")
print(into_3d_array, end="\n\n")


#---Q5
# Flatten the 3-D array into a 2-D sequence
flat_sequence = into_3d_array.flatten()
flat_2d_array = flat_sequence.reshape((5, 3), order='F')

print("2D array:")
print(flat_2d_array, end="\n\n")


#---Q6
# Given two arrays
a = np.array([12, 5, 7, 15, 3, 1, 8])
b = np.array([14, 6, 3, 11, 19, 12, 5])

# Using np.setdiff1d to find elements in 'a' that are NOT in 'b'
remove_array = np.setdiff1d(a, b)

# Print the resulting array
print("Unqiue Array:")
print(remove_array, end="\n\n")


#---Q7
file_path = 'Module6_Data.csv'
# Import the data into a pandas DataFrame
try:
    df = pd.read_csv(file_path)
    print(df)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")



#--
nyc_consumption = 'NYC Consumption(Million gallons per day)'

# Finding the maximum consumption
max_consumption = df[nyc_consumption].max()

print(f"Maximum yearly NYC consumption of water: {max_consumption:.2f} Million Gallons per Day", end="\n\n")

# Getting the number of rows which represents the number of years
num_years = df.shape[0]

print(f"Number of calendar years represented in the data set: {num_years}", end="\n\n")

per_capita_col = 'Per Capita(Gallons per person per day)'
# Calculate the mean
mean_per_capita = df[per_capita_col].mean()

# Calculate the standard deviation
std_dev_per_capita = df[per_capita_col].std()

print(f"Mean per capita daily water consumption: {mean_per_capita:.2f} Gallons")
print(f"Standard deviation of per capita daily water consumption: {std_dev_per_capita:.2f} Gallons", end="\n\n")

nyc_population = 'New York City Population'

# Use NumPy's diff function to calculate the year-to-year differences in population
pop_diff = np.diff(df[nyc_population])

print("Increase or decrease in population from year to year:")
print(pop_diff)
