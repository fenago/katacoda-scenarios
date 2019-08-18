In addition to support for multiple chaincode languages, you can also issue a flag that will bring up a five node Raft ordering service or a Kafka ordering service instead of the one node Solo orderer. For more information about the currently supported ordering service implementations, check out The Ordering Service.

To bring up the network with a Raft ordering service, issue:
`./byfn.sh up -o etcdraft`

To bring up the network with a Kafka ordering service, issue:
`./byfn.sh up -o kafka`

#### Logs
You can scroll through these logs to see the various transactions.

```
Starting for channel 'mychannel' with CLI timeout of '10' seconds and CLI delay of '3' seconds
Continue? [Y/n]
proceeding ...
Creating network "net_byfn" with the default driver
Creating peer0.org1.example.com
Creating peer1.org1.example.com
Creating peer0.org2.example.com
Creating orderer.example.com
Creating peer1.org2.example.com
Creating cli

Channel name : mychannel
Creating channel...
The logs will continue from there. This will launch all of the containers, and then drive a complete end-to-end application scenario. Upon successful completion, it should report the following in your terminal window:

==========================================================

Query Result: 90
2017-05-16 17:08:15.158 UTC [main] main -> INFO 008 Exiting.....
===================== Query successful on peer1.org2 on channel 'mychannel' =====================

===================== All GOOD, BYFN execution completed =====================```
```