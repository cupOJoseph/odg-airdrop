import pandas as pd 
from decimal import Decimal

df = pd.read_csv("odg_airdrop_unweighted.csv", header=0)

total_weight = 923440

for i, row in df.iterrows():
    old_val = row["weight"]
    df.at[i, 'weight'] = (Decimal(row["weight"]) / Decimal(total_weight) * Decimal("300000") * Decimal("10") ** 18).quantize(Decimal("1"))
    df.at[i, 'weight'] = int(df.at[i, 'weight'])
    if i % 1000 == 0:
        print(f"calculated {i}. {old_val} now = {df.at[i, 'weight']}")

df.to_csv('final_odg_airdrop.csv', index=False, header=False)






