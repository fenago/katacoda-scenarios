
In this step, we will learn peer chaincode list command.

The peer chaincode list command allows administrators to list the chaincodes installed on a peer or the chaincodes instantiated on a channel of which the peer is a member.

#### List Syntax
The peer chaincode list command has the following syntax:

```
peer chaincode list [--installed|--instantiated -C <channel-name>]
```


Here are some examples of the peer chaincode list command:
`peer chaincode list  --installed`{{execute T3}}

`peer chaincode list  --instantiated   -C acmechannel`{{execute T3}}