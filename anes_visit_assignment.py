import pandas as pd
import numpy as np

# Read the Excel file
df = pd.read_excel('anes_for_test_01.xlsx')

# Select specific names in a specific column
column_name = '科部'  # Replace with the name of your specific column
specific_names = ['CVS']  # Replace with the specific names of interest
selected_rows = df[df[column_name].isin(specific_names)]

# Print the selected rows
print("Selected Rows:")
print(selected_rows)

# Select rows with specific names in a specific column
unselected_rows = df[~df[column_name].isin(specific_names)]

# Count the unselected rows
unselected_count = len(unselected_rows)
print("Count of unselected rows:", unselected_count)

# Rearrange the unselected rows based on a specific column
specific_column = '病房床號'  # Replace with the specific column to rearrange
unselected_rows = unselected_rows.sort_values(by=specific_column)

# Get input for the number of groups
num_groups = int(input("Enter the number of groups to separate the unselected rows: "))

# Calculate the number of rows per group
rows_per_group = int(np.ceil(unselected_count / num_groups))

# Separate the unselected rows into the input number of groups
group_column = 'Group'
unselected_rows[group_column] = np.repeat(range(num_groups), rows_per_group)[:unselected_count]

# Input the names of the groups to replace the group numbers
group_names = []
for i in range(num_groups):
    group_name = input(f"Enter the name for group {i+1}: ")
    group_names.append(group_name)

# Replace the group numbers with group names
unselected_rows[group_column] = unselected_rows[group_column].map(lambda x: group_names[x])

# Print both the selected and unselected rows
print("Selected Rows:")
print(selected_rows)
print("Unselected Rows:")
print(unselected_rows)