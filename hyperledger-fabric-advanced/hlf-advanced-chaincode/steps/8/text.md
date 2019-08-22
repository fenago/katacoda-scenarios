
In this step, we will learn peer chaincode Query & Invoke commands.

#### Chaincode Query
The peer chaincode query command allows the chaincode to be queried by calling the Invoke method on the chaincode. The difference between the query and the invoke subcommands is that, on successful response, invoke proceeds to submit a transaction to the orderer whereas query just outputs the response, successful or otherwise, to stdout.

The peer chaincode query command has the following syntax:
```
peer chaincode query [flags]
```

Here is an example of the peer chaincode query command, which queries the peer ledger for the chaincode named acmechannel for the value of variable a
`peer chaincode query -C acmechannel -n gocc  -c '{"Args":["query","a"]}'`{{execute T3}}


#### Chaincode Invoke
The peer chaincode invoke command allows administrators to call chaincode functions on a peer using the supplied arguments. The CLI invokes chaincode by sending a transaction proposal to a peer. The peer will execute the chaincode and send the endorsed proposal response (or error) to the CLI. On receipt of a endorsed proposal response, the CLI will construct a transaction with it and send it to the orderer.

The peer chaincode invoke command has the following syntax:
```
peer chaincode invoke [flags]
```

`peer chaincode invoke -C acmechannel -n gocc  -c '{"Args":["invoke","a","b","10"]}'`{{execute T3}}
