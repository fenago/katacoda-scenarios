Chaincode is a program, written in Go, node.js, or Java that implements a prescribed interface. Chaincode runs in a secured Docker container isolated from the endorsing peer process. Chaincode initializes and manages the ledger state through transactions submitted by applications.

In the following sections, we will explore chaincode through the eyes of an application developer. We’ll present a simple chaincode sample application and walk through the purpose of each method in the Chaincode Shim API.

#### Chaincode API
Every chaincode program must implement the Chaincode interface whose methods are called in response to received transactions. You can find the reference documentation of the Chaincode Shim API for different languages below:
1. Go
2. node.js
3. Java

In each language, the Invoke method is called by clients to submit transaction proposals. This method allows you to use the chaincode to read and write data on the channel ledger.