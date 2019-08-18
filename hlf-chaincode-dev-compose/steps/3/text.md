In this step, we will build & start the chaincode. First, get docker exec into chaincode container by running following command:
`docker exec -it chaincode bash`{{execute T1}}

You should see the following:
```
root@d2629980e76b:/opt/gopath/src/chaincode#
```

Now, compile your chaincode:
`cd sacc`{{execute T1}}
`go build`{{execute T1}}

Now run the chaincode:
`CORE_PEER_ADDRESS=peer:7052 CORE_CHAINCODE_ID_NAME=mycc:0 ./sacc`{{execute T1}}