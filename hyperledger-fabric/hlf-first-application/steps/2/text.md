This next section requires you to be in the fabcar subdirectory within your local clone of the fabric-samples repo.

Launch your network using the `startFabric.sh` shell script. This command will spin up a blockchain network comprising peers, orderers, certificate authorities and more. It will also install and instantiate a javascript version of the FabCar smart contract which will be used by our application to access the ledger. We’ll learn more about these components as we go through the tutorial.
`cd fabcar && ./startFabric.sh javascript`{{execute T1}}


**Note:** Wait for the above script to complete before proceeding to next step. It will take around four minutes.