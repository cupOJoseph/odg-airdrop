import pandas as pd 

df = pd.read_csv("odg_airdrop_unweighted.csv")

total_weight = df.iloc[:,1].sum()
print(f"total weight {total_weight}")

multiplier = 300000 / total_weight 

df["token_amount"] = df.iloc[1, 1] * multiplier

df.iloc[:, [0, 2]].to_csv('final_odg_airdrop.csv', index=False, header=False)






