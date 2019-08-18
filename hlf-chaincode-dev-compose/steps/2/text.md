
Chaincode is a program, written in Go, node.js, or Java that implements a prescribed interface. Chaincode runs in a secured Docker container isolated from the endorsing peer process. Chaincode initializes and manages the ledger state through transactions submitted by applications.


In this step, we will run chaincode using docker-cmpose, navigate to the chaincode-docker-devmode directory of the fabric-samples clone:

`cd chaincode-docker-devmode`{{execute T1}}

`cd chaincode-docker-devmode`{{execute T111}}
`cd chaincode-docker-devmode`{{execute A1}}

Now open three terminals and navigate to your chaincode-docker-devmode directory in each.

Run following command to start the network
`docker-compose -d -f docker-compose-simple.yaml up`{{execute T1}}