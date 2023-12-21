# ODG Airdrop

## Using this repo
1. List of target groups is psuedo code for who should be included
2. full.csv is a complete list of addresses that shall be included
3. Other csv lists shall be combined to create the full.csv file
4. Weights and token amounts based on overlapping in mutliple lists shall be calculated with a script


## List of target groups
1. Reflexer Vault Users
2. RAI/ETH LPs
3. OD testnet users
5. Arbitrum DAO voters
6. Arbitrum CDP users of other competing protocols
7. Arbitrum LST bridgers
8. LST LPs on Arbitrum
9. Meta Cartel members
10. LDO and RPL voters

### Potential ideas
1. Raft victims
2. HAI testnet users
3. Geode testnet users
4. Rocket Pool Solo Stakers

## Methology
1. Assign a point number to each list. RAI vault users get 10 points each. OD Testnet users get 5 points each.
2. Add points for accounts that are in multiple lists for an account total
3. ODG per account = (accounts point / total points for the list) * total ODG airdrop amount
