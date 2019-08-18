
Chaincode is a program, written in Go, node.js, or Java that implements a prescribed interface. Chaincode runs in a secured Docker container isolated from the endorsing peer process. Chaincode initializes and manages the ledger state through transactions submitted by applications.


In this step, we will run chaincode using docker-cmpose, navigate to the chaincode-docker-devmode directory of the fabric-samples clone:
`cd chaincode-docker-devmode`{{execute T1}}

We will use three different terminals for following:
1. Start the network
2. Build & start the chaincode
3. Use the chaincode

Run following command to start the network
`docker-compose -f docker-compose-simple.yaml up`{{execute T1}}