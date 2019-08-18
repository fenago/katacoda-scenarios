Even though you are in --peer-chaincodedev mode, you still have to install the chaincode so the life-cycle system chaincode can go through its checks normally. This requirement may be removed in future when in --peer-chaincodedev mode.

We’ll leverage the CLI container to drive these calls.
`docker exec -it cli bash`{{execute T2}}

`peer chaincode install -p chaincodedev/chaincode/sacc -n mycc -v 0`{{execute T2}}
`peer chaincode instantiate -n mycc -v 0 -c '{"Args":["a","10"]}' -C myc`{{execute T2}}

Now issue an invoke to change the value of “a” to “20”.
`peer chaincode invoke -n mycc -c '{"Args":["set", "a", "20"]}' -C myc`{{execute T2}}

#### Testing chaincode
Finally, query a. We should see a value of 20.
`peer chaincode query -n mycc -c '{"Args":["query","a"]}' -C myc`{{execute T2}}

#### Chaincode access control
Chaincode can utilize the client (submitter) certificate for access control decisions by calling the GetCreator() function. Additionally the Go shim provides extension APIs that extract client identity from the submitter’s certificate that can be used for access control decisions, whether that is based on client identity itself, or the org identity, or on a client identity attribute.