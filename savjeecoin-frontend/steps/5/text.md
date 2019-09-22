#### Generate a keypair
To make transactions on this blockchain you need a keypair. The public key becomes your wallet address and the private key is used to sign transactions.

```
const EC = require('elliptic').ec;
const ec = new EC('secp256k1');

const myKey = ec.genKeyPair();
```

The myKey object now contains your public & private key:
```
console.log('Public key:', myKey.getPublic('hex'));
console.log('Private key:', myKey.getPrivate('hex'));
```

#### Create a blockchain instance
Now you can create a new instance of a Blockchain:

```
const {Blockchain, Transaction} = require('savjeecoin');

const myChain = new Blockchain();
Adding transactions
// Transfer 100 coins from my wallet to "toAddress"
const tx = new Transaction(myKey.getPublic('hex'), 'toAddress', 100);
tx.signTransaction(myKey);

myChain.addTransaction(tx);
```

To finalize this transaction, we have to mine a new block. We give this method our wallet address because we will receive a mining reward:

```
myChain.minePendingTransactions(myKey.getPublic('hex'));
```
