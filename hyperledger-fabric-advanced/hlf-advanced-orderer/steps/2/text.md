In this exercise you will talk about the orderer in the hyperledger fabric. We will learn to configure your node using `orderer.yaml`

Many distributed blockchains, such as Ethereum and Bitcoin, are not permissioned, which means that any node can participate in the consensus process, wherein transactions are ordered and bundled into blocks. 

These systems rely on probabilistic consensus algorithms which eventually guarantee ledger consistency to a high degree of probability, but which are still vulnerable to divergent ledgers (also known as a ledger “fork”), where different participants in the network have a different view of the accepted order of transactions.

In the next steps, we will install **cryptogen** to generate crypto material and **configtxgen** utility for generating genesis block. At the end, we will also launch an orderer.

