In this step, we will learn peer chaincode status.

The peer chaincode install command allows administrators to install chaincode onto the filesystem of a peer.

#### Install Syntax
The peer chaincode install command has the following syntax:
```
peer chaincode install [flags]
```

#### Install Code
`peer chaincode install -n gocc -v 1.0  -p chaincode_example02`{{execute T3}} 


#### Instantiate Code
The peer chaincode instantiate command allows administrators to instantiate chaincode on a channel of which the peer is a member.

The peer chaincode instantiate command has the following syntax:
```
peer chaincode instantiate [flags]
```

`peer chaincode instantiate  -n gocc -v 1.0 -C acmechannel -c '{"Args":["init","a","100","b","200"]}'`{{execute T3}}

**Note:** Please wait for the few seconds for the above command to get response.