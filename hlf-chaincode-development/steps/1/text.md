Chaincode is a program, written in Go, node.js, or Java that implements a prescribed interface. Chaincode runs in a secured Docker container isolated from the endorsing peer process. Chaincode initializes and manages the ledger state through transactions submitted by applications.

A chaincode typically handles business logic agreed to by members of the network, so it similar to a “smart contract”. A chaincode can be invoked to update or query the ledger in a proposal transaction. Given the appropriate permission, a chaincode may invoke another chaincode, either in the same channel or in different channels, to access its state. Note that, if the called chaincode is on a different channel from the calling chaincode, only read query is allowed. That is, the called chaincode on a different channel is only a Query, which does not participate in state validation checks in subsequent commit phase.

In the following sections, we will explore chaincode through the eyes of an application developer. We’ll present a simple chaincode sample application and walk through the purpose of each method in the Chaincode Shim API.

Chaincode API
Every chaincode program must implement the Chaincode interface whose methods are called in response to received transactions. You can find the reference documentation of the Chaincode Shim API for different languages below:

Go
node.js
Java
In each language, the Invoke method is called by clients to submit transaction proposals. This method allows you to use the chaincode to read and write data on the channel ledger.

In this step, we will clone fabric samples repository.

#### Clone fabric samples repository
`git clone https://github.com/hyperledger/fabric-samples.git`{{execute}}


#### Install prerequisites
Before we begin, let's install all the Prerequisites on the platform(s) on which you’ll be developing blockchain applications and/or operating Hyperledger Fabric.

Now, move in the directory into which you will install the Fabric Samples and binaries, go ahead and execute the command to pull down the binaries and images.
`cd fabric-samples && curl -sSL http://bit.ly/2ysbOFE | bash -s`{{execute}}


The build your first network (BYFN) scenario provisions a sample Hyperledger Fabric network consisting of two organizations, each maintaining two peer nodes. It also will deploy a “Solo” ordering service by default,though other ordering service implementations are available.

You will notice that there are a number of samples included in the fabric-samples repository. We will be using the first-network sample. Let’s open that sub-directory now.

`cd first-network`{{execute}}

**Note:**
The supplied commands in this documentation MUST be run from your first-network sub-directory of the fabric-samples repository clone. If you elect to run the commands from a different location, the various provided scripts will be unable to find the binaries.