In this exercise you will talk about the orderer in the hyperledger fabric. We will learn to configure your node using `orderer.yaml`

Kafka is primarily a distributed, horizontally-scalable, fault-tolerant, commit log. A commit log is basically a data structure that only appends. No modification or deletion is possible, which leads to no read/write locks, and the worst case complexity O(1). There can be multiple Kafka nodes in the blockchain network, with their corresponding Zookeeper ensemble.

- High ThroughPut
- Durable 
- Highly Scalable
- High Performance

In the next steps, we will install kafka, zookeeper and JRE8.
