# ODG Airdrop

## Using this repo
1. List of target groups is psuedo code for who should be included
2. full.csv is a complete list of addresses that shall be included
3. Other csv lists shall be combined to create the full.csv file
4. Weights and token amounts based on overlapping in mutliple lists shall be calculated with a script


## Methology
1. Assign a point number (weight) to each list. 
2. Add weights for accounts that are in multiple lists for an account total
3. ODG per account = (accounts weight / total weight for the list) * total ODG airdrop amount 
