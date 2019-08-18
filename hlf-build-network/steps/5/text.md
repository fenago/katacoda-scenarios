Finally, let’s bring it all down so we can explore the network setup one step at a time. The following will kill your containers, remove the crypto material and four artifacts, and delete the chaincode images from your Docker Registry:

`./byfn.sh down`{{execute}}

Once again, you will be prompted to continue, respond with a y or hit the return key:

Stopping with channel 'mychannel' and CLI timeout of '10'
Continue? [Y/n] y
proceeding ...
WARNING: The CHANNEL_NAME variable is not set. Defaulting to a blank string.
WARNING: The TIMEOUT variable is not set. Defaulting to a blank string.
Removing network net_byfn
468aaa6201ed
...
Untagged: dev-peer1.org2.example.com-mycc-1.0:latest
Deleted: sha256:ed3230614e64e1c83e510c0c282e982d2b06d148b1c498bbdcc429e2b2531e91
...
If you’d like to learn more about the underlying tooling and bootstrap mechanics, continue reading. In these next sections we’ll walk through the various steps and requirements to build a fully-functional Hyperledger Fabric network.

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