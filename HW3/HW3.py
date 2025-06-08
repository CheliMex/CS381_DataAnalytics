import pandas as pd
import numpy as np


#-----Q1
# File path
file_path = 'cars-sample35.txt'

# Define the headers
headers = [
    "Price",
    "Maintenance_Cost",
    "Number_of_Doors",
    "Number_of_Passengers",
    "Luggage_Capacity",
    "Safety_Rating",
    "Classification_of_Vehicle"
]

try:
    df = pd.read_csv(file_path, header=None, names=headers)
    print("Data with headers:")
    print(df)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")



#-----Q2
# Extracting attributes into 7 distinct list objects
price_list = df['Price'].tolist()
maintenance_cost_list = df['Maintenance_Cost'].tolist()
number_of_doors_list = df['Number_of_Doors'].tolist()
number_of_passengers_list = df['Number_of_Passengers'].tolist()
luggage_capacity_list = df['Luggage_Capacity'].tolist()
safety_rating_list = df['Safety_Rating'].tolist()
classification_list = df['Classification_of_Vehicle'].tolist()

print("--- Extracted Attributes to Python Lists ---")
print(f"\nPrice List: {price_list}")
print(f"\nMaintenance Cost List: {maintenance_cost_list}")
print(f"\nNumber of Doors List: {number_of_doors_list}")
print(f"\nNumber of Passengers List: {number_of_passengers_list}")
print(f"\nLuggage Capacity List: {luggage_capacity_list}")
print(f"\nSafety Rating List: {safety_rating_list}")
print(f"\nClassification List: {classification_list}")



#-----Q3
# Initialize an empty list to store the indices
med_price = []

# Using enumerate to get both index and value
for index, price in enumerate(price_list):
    # Check if the current price value is "med"
    if price == "med":
        med_price.append(index)

# Printing the index with med price
print("\nIndex value with 'med' price:")
print(med_price)



#-----Q4
# Initialize an empty list to store the passenger counts
num_passengers = []

# Use the index to retrieve 'Number_of_Passengers' from its list
for index in med_price:
    num_passengers.append(number_of_passengers_list[index])

# Printing the value for autos with med price
print("\n'Number of passengers' for autos with 'med' price:")
print(num_passengers)



#-----Q5
# Initialize an empty list to store the indices
high_price_not_low_maintenance = []

# Iterate using a range to get indices, as we need to access two lists at the same time
for i in range(len(price_list)):
    # Check both conditions: price is "high" AND maintenance is NOT "low"
    if price_list[i] == "high" and maintenance_cost_list[i] != "low":
        high_price_not_low_maintenance.append(i)

# Printing the indices of autos with 'high' price AND maintenance value NOT 'low
print("\nIndices of autos with 'high' price AND maintenance NOT 'low':")
print(high_price_not_low_maintenance)



#-----Q6
# This iterates through (index, price) pairs from enumerate(price_list)
# and includes 'index' in the new list only if 'price' is "med".
index_med_price_list_comp = [
    index for index, price in enumerate(price_list) if price == "med"]

# Printing the indices of automobiles with 'med' price
print("\nIndices of automobiles with 'med' price:")
print(index_med_price_list_comp)



#-----Q7
# This gets the 'number_of_passengers_list[index]' for each (index, price) pair
# where 'price' is "med".
num_passengers_med_price_list_comp = [
    number_of_passengers_list[index] for index, price in enumerate(price_list) if price == "med"]

# Printing the number of passengers for autos with price value of 'med'
print("\n'Number of passengers' for autos with 'med' price:")
print(num_passengers_med_price_list_comp)



#-----Q8
# This uses zip to iterate through (index, price, maintenance) 3 things simultaneously.
# 'i' (the index) is included only if 'price' is "high" AND 'maintenance' is NOT "low".

high_price_not_low_maintenance_list_comp = [
    i for i, (price, maintenance) in enumerate(zip(price_list, maintenance_cost_list))
    if price == "high" and maintenance != "low"
]

# Printing the indices of autos with 'high' price AND maintenance value NOT 'low'
print("\nIndices of autos with 'high' price AND maintenance NOT 'low':")
print(high_price_not_low_maintenance_list_comp)




#-----Q1
# Initialize a list to store the data list
nlist = [ 
    [1, 2, 3], 
    ['A', 'B', 'C'], 
    [4, 5], 
    ['D', 'E'] 
]

# Flattens the list of lists into a single list
flattened_list = [item for sublist in nlist for item in sublist]

# Print each individual element of the component lists
print(f"\nFlattened list (using list comprehension): {flattened_list}")
