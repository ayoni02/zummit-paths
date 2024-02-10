import pandas as pd

# Read the CSV file
def read_csv(file):
    return pd.read_csv(file)

# Call the function into df
df = read_csv('data.csv')