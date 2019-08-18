In this step, we will build & start the chaincode. First, get docker exec into chaincode container by running following command:
`docker exec -it chaincode bash`{{execute T2}}

You should see the following:
```
root@d2629980e76b:/opt/gopath/src/chaincode#
```

Now, compile your chaincode:
`cd sacc`{{execute T2}}

`go build`{{execute T2}}

You can view the contents of the `sacc.go` file by running `cat sacc.go`{{execute T2}}. The code has been covered in [Chaincode for Developers](https://www.katacoda.com/ernesto/courses/hyperledger-fabric/hlf-chaincode-development) scenario in detail.

Now run the chaincode:
`CORE_PEER_ADDRESS=peer:7052 CORE_CHAINCODE_ID_NAME=mycc:0 ./sacc`{{execute T2}}