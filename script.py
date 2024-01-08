import pandas as pd
import os
from web3 import Web3

# List of CSV files
csv_files = ['OD.csv', 'RAI.csv', 'cdp-users.csv', 'reth.csv', 'wsteth.csv', 'metacartel.csv', 'camelot.csv', 'jasmine.csv', 'dsentra.csv', 'delegators.csv']  # Add more CSVs as needed

# List to store dataframes
weights = [1000, 125, 75, 25, 25, 25, 50, 25, 25, 1]
print("weights set")

counter = 0
def calculate_checksum(address):
    w3 = Web3()
    global counter
    counter += 1
    if(counter % 1000 == 0):
        print(f"Check summed {counter}")
    return w3.to_checksum_address(address)

# Concatenate dataframes along the rows
concatenated_df = pd.DataFrame(columns=['address'])

# Iterate through the list of CSV files and concatenate them
i = 0

for file in csv_files:
    file_path = os.path.join('lists/', file)  # Replace 'path_to_directory_containing_csv_files' with the actual path
    df = pd.read_csv(file_path, header=None, names=['address'])
    df['weight'] = weights[i]
    i = i + 1
    concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
    print("contatinating...")
#theres now 1 dataframe with lots of weights and duplicates 
print("concatenated")

# Apply the calculate_checksum function to each value in 'column1'
concatenated_df['address'] = concatenated_df['address'].apply(calculate_checksum)
print("checksum complete")

##remove duplcates and apply weights by adding for each checksummed address
# Group by 'address' and sum the 'weight' for each group
aggregated_df = concatenated_df.groupby('address')['weight'].sum().reset_index()

aggregated_df.to_csv("odg_airdrop.csv", index=False)

print("done")
# save the first 100 rows to a csv thats easy to open quickly and check stuff
aggregated_df.head(200).to_csv("short_test_result100.csv", index=False)



