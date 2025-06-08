import numpy as np
import pandas as pd
import re

my_data = r"555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
#---Q1
# 1. Create a Pandas Series and put it in a list to be treated as one element
data_series = pd.Series([my_data])

# 2. The pattern for one or more digits
num_series = data_series.str.findall(r"\d+")

# To get the actual list of numbers out of the string
extract_numbers = num_series[0]
print("Extract Numbers:")
print(extract_numbers, end="\n\n")

#---Q2
# 1. The pattern for one or more characters that are NOT digits, hyphens, or parentheses.
name_pattern = r"[^0-9()-]+"

name_series = data_series.str.findall(name_pattern)
extract_names = name_series[0]
#print(extract_names)

# 2. Remove any whitespace and filter out empty strings
clean_names = []
for segment in extract_names:
    temp_name = segment.replace('\\', '')
    temp_name = re.sub(r'\s+', ' ', temp_name)
    # 3. Trim leading/trailing spaces
    temp_name = temp_name.strip()
    # 4. Filter empty strings and name is more than 2 characters
    if temp_name and len(temp_name) > 2:
        clean_names.append(temp_name)

print("Extract Names:")
print(clean_names, end="\n\n")

#---Q3
names_series = pd.Series(clean_names)
rearranged_names = []

for name in names_series:
    if ',' in name:
        #1. Split by comma
        parts = [p.strip() for p in name.split(',')]
        #2. At least two parts (last, first/middle)
        if len(parts) >= 2:
            #3. Join all parts after the first (firstname, middlename) and then add lastname
            first_middle_part = " ".join(parts[1:])
            last_name_part = parts[0]
            rearranged_name = f"{first_middle_part} {last_name_part}"
        else:
            rearranged_name = name # Fallback if comma split fails
    else:
        #4. Names without a comma are assumed to be already in order
        rearranged_name = name

    rearranged_names.append(rearranged_name)

print("Rearrange Names:")
print(rearranged_names, end="\n\n")

#---Q4
#1. titles with 
titles = ["Dr.", "Rev."]

#2. Create logical vector
has_title = []
for name in rearranged_names:
    found_title = False
    for title in titles:
        if name.startswith(title):
            found_title = True
            break # No need to check other titles if one is found
    has_title.append(found_title)

print("Logical vector with title:")
print(has_title, rearranged_names, end="\n\n")

#3. Convert to a Pandas Series for a true "logical vector"
#has_title_series = pd.Series(has_title, rearranged_names)
#print(has_title_series)

#---Q5
has_middle_name = []

for name in rearranged_names:
    #1. Split the name into parts by space
    parts = name.split()
    
    #2. Adjust count for titles
    adjusted_parts_count = len(parts)
    for title in titles:
        #3. Check if the first word of the name is a title
        if parts and parts[0] == title.strip('.'): # Compare "Dr" with "Dr." after stripping period
            adjusted_parts_count -= 1 # Reduce count if it's a title
            break # Assume only one title per person
        # Handle "Dr." or "Rev." specifically as a full word with period
        if parts and parts[0] == title:
            adjusted_parts_count -= 1
            break
            
    # If, after accounting for titles there are more than 2 parts then it has a middle name.  
    if adjusted_parts_count > 2:
        has_middle_name.append(True)
    else:
        has_middle_name.append(False)
        
print("Logical vector with middle name:")
print(has_middle_name, rearranged_names, end="\n\n")

# Convert to a Pandas Series for the logical vector
#has_middle_name_series = pd.Series(has_middle_name, rearranged_names)
#print(has_middle_name_series)

#---Q6
print("It doesn't stop at the first '>' because the '.+' is greedy. It will continue to match until it absolutely has to stop to which then stops at '>' in the pattern to match. The '.' matches any single character (except for a newline character)The '+' matches one or more element, so by putting them together it literally means match one or more of any character (except newline). Therefore it will look at the entire string. We can correct it by '?' which will match as few as possible allowing the rest of the pattern to match.The new Regex will be <.+?> ", end="\n\n")


#---Q7
print("'^' = negation (not) when inside a bracket [], especially if its in the begining. The Regex mean match any character that is NOT a digit (0-9) and =+*(). The problem here is that we want to include the '^' as well, so we will add it at the end along with the other symbols. The new Regex will be [0-9=+\-*()^]+")
