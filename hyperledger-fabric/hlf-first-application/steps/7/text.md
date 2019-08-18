The application starts by bringing in scope two key classes from the fabric-network module; FileSystemWallet and Gateway. These classes will be used to locate the user1 identity in the wallet, and use it to connect to the network:
```
const { FileSystemWallet, Gateway } = require('fabric-network');
```

The application connects to the network using a gateway:
```
const gateway = new Gateway();
await gateway.connect(ccp, { wallet, identity: 'user1' });
```

This code creates a new gateway and then uses it to connect the application to the network. ccp describes the network that the gateway will access with the identity user1 from wallet. See how the ccp has been loaded from ../../basic-network/connection.json and parsed as a JSON file:
```
const ccpPath = path.resolve(__dirname, '..', '..', 'basic-network', 'connection.json');
const ccpJSON = fs.readFileSync(ccpPath, 'utf8');
const ccp = JSON.parse(ccpJSON);
```

A network can be divided into multiple channels, and the next important line of code connects the application to a particular channel within the network, mychannel:
```
const network = await gateway.getNetwork('mychannel');
```

Within this channel, we can access the smart contract fabcar to interact with the ledger:
```
const contract = network.getContract('fabcar');
```

Within fabcar there are many different transactions, and our application initially uses the queryAllCars transaction to access the ledger world state data:
```
const result = await contract.evaluateTransaction('queryAllCars');
```

The evaluateTransaction method represents one of the simplest interaction with a smart contract in blockchain network. It simply picks a peer defined in the connection profile and sends the request to it, where it is evaluated. The smart contract queries all the cars on the peer’s copy of the ledger and returns the result to the application. This interaction does not result in an update the ledger.