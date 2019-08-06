Run this command to submit a transaction to transfer 20 LBR from Alice’s account to Bob’s account:
`transfer 0 1 20`{{execute}}

- 0 is the index of Alice’s account.
- 1 is the index of Bob’s account.
- 20 is the number of Libra to transfer from Alice’s account to Bob’s account.

Sample output on success:

```
>> Transferring
Transaction submitted to validator
To query for transaction status, run: query txn_acc_seq 0 0 <fetch_events=true|false>
```

# Transaction Status
You can use the command `query txn_acc_seq 0 0 true`{{execute}} to retrieve the information about the transaction you just submitted.
- First parameter is the local index of the sender account
- Second parameter is the sequence number of the account. 


# Sequence Number
Run the following commands to get the sequence number of both accounts:
`query sequence 0`{{execute}}

`query sequence 1`{{execute}}

Sequence number of 1 for Alice’s account (index 0) indicates that one transaction has been sent from Alice’s account so far. 

# Check Balance
Run the following commands to check the final balance of both accounts:
`query balance 0`{{execute}}

`query balance 1`{{execute}}