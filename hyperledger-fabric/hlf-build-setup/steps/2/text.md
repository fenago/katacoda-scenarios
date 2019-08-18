We will run a bash script — `byfn.sh` — that leverages these Docker images to quickly bootstrap a Hyperledger Fabric network that by default is comprised of four peers representing two different organizations, and an orderer node. It will also launch a container to run a scripted execution that will join peers to a channel, deploy a chaincode and drive execution of transactions against the deployed chaincode.

Here’s the help text for the byfn.sh script:
- 'up' - bring up the network with docker-compose up"
- 'down' - clear the network with docker-compose down"
- 'restart' - restart the network"
- 'generate' - generate required certificates and genesis block"
- 'upgrade'  - upgrade the network from version 1.3.x to 1.4.0"
-  -v - verbose mode"
- byfn.sh -h (print this message)"

Typically, one would first generate the required certificates and
genesis block, then bring up the network. e.g.:
```
  byfn.sh generate -c mychannel"
  byfn.sh up -c mychannel -s couchdb"
  byfn.sh up -c mychannel -s couchdb -i 1.4.0"
  byfn.sh up -l node"
  byfn.sh down -c mychannel"
  byfn.sh upgrade -c mychannel"

Taking all defaults:"
      byfn.sh generate"
      byfn.sh up"
      byfn.sh down"
```

If you choose not to supply a flag, the script will use default values.

#### Generate Network Artifacts
Ready to give it a go? Okay then! Execute the following command:
`./byfn.sh generate`{{execute}}

You will see a brief description as to what will occur, along with a yes/no command line prompt. Respond with a y or hit the return key to execute the described action.

```
Generating certs and genesis block for channel 'mychannel' with CLI timeout of '10' seconds and CLI delay of '3' seconds
Continue? [Y/n] y
proceeding ...
/Users/xxx/dev/fabric-samples/bin/cryptogen
```

This first step generates all of the certificates and keys for our various network entities, the genesis block used to bootstrap the ordering service, and a collection of configuration transactions required to configure a Channel.