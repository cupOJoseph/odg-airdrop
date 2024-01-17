import pandas as pd 

df = pd.read_csv("odg_airdrop_unweighted.csv", header=0)

total_weight = 923440

for i, row in df.iterrows():
    old_val = row["weight"]
    df.at[i, 'weight'] = (row["weight"] / total_weight) * 300000 * 10 ** 18
    if i % 1000 == 0:
        print(f"calculated {i}. {old_val} now = {df.at[i, 'weight']}")

df.to_csv('final_odg_airdrop.csv', index=False, header=False)






