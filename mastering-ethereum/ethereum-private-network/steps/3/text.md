You can create unlimited accounts with Geth, as they are generated from an algorithm known as Rivest Shamir Adleman (RSA) that creates the public and private keys off-chain. The number of possible combinations is so big that it is nearly impossible to generate the exact same account as another user. To generate an account with Geth, run the following command:

`geth account new`{{execute}}

This will ask you for a password to keep your credentials safe. 

After that, execute the following command:
`puppeth`{{execute}}

This results in the following output:

![](https://github.com/fenago/katacoda-scenarios/raw/master/mastering-ethereum/ethereum-private-network/steps/3/cli.JPG)


It may ask you for a network to administer. In that case, just type a random name for the new network that you want to create:

![](https://github.com/fenago/katacoda-scenarios/raw/master/mastering-ethereum/ethereum-private-network/steps/3/genesis.JPG)


Then, choose the second option to create a new genesis file:

![](https://github.com/fenago/katacoda-scenarios/raw/master/mastering-ethereum/ethereum-private-network/steps/3/genesis.JPG)

Create a new genesis file from scratch and choose the first consensus engine, proof-of-work.
Now, it will ask you which accounts should be pre-funded. Here's where you'll paste the account address that you copied after generating a new address with the geth command previously:

![](https://github.com/fenago/katacoda-scenarios/raw/master/mastering-ethereum/ethereum-private-network/steps/3/fund.JPG)
