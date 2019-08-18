This next section requires you to be in the fabcar subdirectory within your local clone of the fabric-samples repo, navigate to the `fabcar` directory of the fabric-samples clone:
`cd fabcar`{{execute T1}}


Launch your network using the `startFabric.sh` shell script. This command will spin up a blockchain network comprising peers, orderers, certificate authorities and more. It will also install and instantiate a javascript version of the FabCar smart contract which will be used by our application to access the ledger. We’ll learn more about these components as we go through the tutorial.
`./startFabric.sh javascript`{{execute T1}}

Alright, you’ve now got a sample network up and running, and the FabCar smart contract installed and instantiated. Let’s install our application pre-requisites so that we can try it out, and see how everything works together.

We will use three differentterminals for following:
1. Start the network
2. Build & start the chaincode
3. Use the chaincode

Run following command to start the network
`docker-compose -f docker-compose-simple.yaml up`{{execute T1}}