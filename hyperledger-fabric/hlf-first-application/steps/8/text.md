From an application perspective, updating the ledger is simple. An application submits a transaction to the blockchain network, and when it has been validated and committed, the application receives a notification that the transaction has been successful. 


Under the covers this involves the process of consensus whereby the different components of the blockchain network work together to ensure that every proposed update to the ledger is valid and performed in an agreed and consistent order.

Our first update to the ledger will create a new car. We have a separate program called invoke.js that we will use to make updates to the ledger. Run `cat invoke.js`{{execute T1}} to see how we constructed our transaction and submit it to the network:
```
await contract.submitTransaction('createCar', 'CAR10', 'Honda', 'Accord', 'Black', 'Tom');
```

See how the applications calls the smart contract transaction createCar to create a black Honda Accord with an owner named Tom. We use CAR10 as the identifying key here, we don’t need to use sequential keys.

`node invoke.js`{{execute T1}}

**Note:** If the invoke is successful, you will see output like this:
```
Wallet path: /root/fabric-samples/fabcar/javascript/wallet
Transaction has been submitted
```