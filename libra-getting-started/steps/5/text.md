In this step, we will add coins to both accounts created earlier.

Minting and adding coins to accounts on testnet is done via Faucet. Faucet is a service that runs along with the testnet. This service only exists to facilitate minting coins for testnet and will not exist for mainnet. It creates Libra with no real-world value. 

# Add Coins
To mint Libra and add to Alice’s account, enter this command:
`account mint 0 110`{{execute}}

- 0 is the index of Alice’s account.
- 110 is the amount of Libra to be added to Alice’s account.

# Task 
To complete this task, add **140** coins to account 1.

```
Hint:
    account mint account_index amount
```

# Check Balance

Run the following commands to check the balance of both accounts:
`query balance 0`{{execute}}

`query balance 1`{{execute}}