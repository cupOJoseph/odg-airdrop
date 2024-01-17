# ODG Airdrop

<img width="1203" alt="Screen Shot 2024-01-17 at 1 48 11 PM" src="https://github.com/cupOJoseph/odg-airdrop/assets/9449596/06b1c3c7-af3c-4626-95a3-0e167ef0829c">

See full [spreadsheet](https://docs.google.com/spreadsheets/d/147OFIAgpuya1MrxR5yWwCwtPLoY8AJ6huYCSGBMZQ8g/edit?usp=sharing).

## Using this repo
1. List of target groups is psuedo code for who should be included
2. final_odg_airdrop.csv is a complete list of addresses that shall be included
3. Other csv lists shall be combined to create the final file
4. Weights and token amounts based on overlapping in mutliple lists shall be calculated with the scripts


## Methology
1. Assign a point number (weight) to each list. 
2. Add weights for accounts that are in multiple lists for an account total
3. ODG per account = (accounts weight / total weight for the list) * total ODG airdrop amount 
