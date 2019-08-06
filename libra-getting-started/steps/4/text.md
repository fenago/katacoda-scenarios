
In this step, we will create two wallet accounts.

## Task 1:  Create Alice’s Account
Note that creating an account using the CLI does not update the blockchain, it just creates a local key-pair.

To create Alice’s account, enter this command:
`account create`{{execute}}

```
>> Creating/retrieving next account from wallet
Created/retrieved account #0 address 5769s5fafae4147b2a105a0be2f81972883441cfaaadf93fc0868e7a0253c4a8
```

- 0 is the index of Alice’s account
- hex string is the address of Alice’s account. 
- index is meaningless to the blockchain. 
- Alice’s account will be created on the blockchain only when either money is added to Alice’s account via minting, or money is transferred to Alice’s account.
- Note that you may also use the hex address in CLI commands.


## Task 2: Create Bob’s Account

To create Bob’s account, repeat the account creation command:
`account create`{{execute}}

1 is the index for Bob’s account, and the hex string is the address of Bob’s account. 

**Note** that creating an account using the CLI does not update the blockchain, it just creates a local key-pair.


## Task 3: List Accounts
To list the accounts you have created, enter this command:
`account list`{{execute}}