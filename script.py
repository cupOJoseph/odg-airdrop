import pandas as pd
import os

# List of CSV files
csv_files = ['OD.csv', 'RAI.csv', 'arb_CDPs.csv', 'wsteth.csv', 'metacartel', 'camelot', 'jasmine']  # Add more CSVs as needed

# List to store dataframes
dfs = [600, 300, 1, 25, 10, 10, 25, 25, 25]

i = 0
def assign_points(csv_path):
    df = pd.read_csv(csv_path, header=None, names=['address'])
    df['points'] = dfs[i]
    i = i + 1
    return df

# Concatenate dataframes along the rows
result_df = pd.concat(dfs, ignore_index=True)

# Group by ID and sum the points
result_df = result_df.groupby('address')['points'].sum().reset_index()

# Save the result to a new CSV
output_csv_path = 'Output_CSV.csv'
result_df.to_csv(output_csv_path, index=False)

print(f"Combined data saved to {output_csv_path}")
