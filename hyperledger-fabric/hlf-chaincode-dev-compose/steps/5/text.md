
In this step, we will update value if `a` to 20. We will also verify that the value was update using peer chaincode query command.

Now issue an invoke to change the value of “a” to “20”.
`peer chaincode invoke -n mycc -c '{"Args":["set", "a", "20"]}' -C myc`{{execute T3}}

#### Testing chaincode
Finally, query a. We should see a value of 20.
`peer chaincode query -n mycc -c '{"Args":["query","a"]}' -C myc`{{execute T3}}

#### Chaincode access control
Chaincode can utilize the client (submitter) certificate for access control decisions by calling the GetCreator() function. Additionally the Go shim provides extension APIs that extract client identity from the submitter’s certificate that can be used for access control decisions, whether that is based on client identity itself, or the org identity, or on a client identity attribute.