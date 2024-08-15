import pandas as pd

"""
    Cleaning the dataset:
    1. Remove $ and , from Annual Salary column
    2. Remove % from Bonus column
    3. Round age to
"""

df = pd.read_csv('employee_data_first.csv')


# Remove $ and , from Annual Salary column
df['Annual Salary'] = df['Annual Salary'].str.replace('[$,]', '', regex=True).str.strip()


# Remove % from Bonus column
df['Bonus %'] = df['Bonus %'].str.replace('%', '')


# Rename columns for readability
df.rename(columns={'Annual Salary': 'Annual Salary ($)', 'Bonus %': 'Bonus (%)'}, inplace=True)


# Remove null values
df.dropna(inplace=True)


# Round values in age column to integers
df['Age'] = df['Age'].astype(int)


# Output to csv
df.to_csv('employee_data_updated.csv', index=False)
