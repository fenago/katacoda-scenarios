Chaincode is a program, written in Go, node.js, or Java that implements a prescribed interface. Chaincode runs in a secured Docker container isolated from the endorsing peer process. Chaincode initializes and manages the ledger state through transactions submitted by applications.

We will use three different terminals in the next steps for the following:
1. Start the network
2. Start the chaincode
3. Use the chaincode


Run `cat fabric-setup.sh`{{execute T1}} to view the contents of the bash script. Copy & execute following command to download and install peer CLI `./fabric-setup.sh`{{execute T1}}

#### Validate
You can verify peer is installed on your System by running `peer  --version`{{execute T1}} command.

#### Usage
Here’s some examples using the different available flags on the peer chaincode command `peer chaincode --help`{{execute T1}}
