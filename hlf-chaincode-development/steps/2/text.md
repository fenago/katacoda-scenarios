Our application is a basic sample chaincode to create assets (key-value pairs) on the ledger.


#### Housekeeping
First, let’s start with some housekeeping. As with every chaincode, it implements the Chaincode interface in particular, Init and Invoke functions. So, let’s add the Go import statements for the necessary dependencies for our chaincode. We’ll import the chaincode shim package and the peer protobuf package. Next, let’s add a struct SimpleAsset as a receiver for Chaincode shim functions.

<pre class="file" data-filename="sacc.go" data-target="replace">
package main

import (
    "fmt"

    "github.com/hyperledger/fabric/core/chaincode/shim"
    "github.com/hyperledger/fabric/protos/peer"
)

// SimpleAsset implements a simple chaincode to manage an asset
type SimpleAsset struct {
}
</pre>


#### Initializing the Chaincode
Next, we’ll implement the Init function.
```
// Init is called during chaincode instantiation to initialize any data.
func (t *SimpleAsset) Init(stub shim.ChaincodeStubInterface) peer.Response {
}
```


Note that chaincode upgrade also calls this function. When writing a chaincode that will upgrade an existing one, make sure to modify the Init function appropriately. In particular, provide an empty “Init” method if there’s no “migration” or nothing to be initialized as part of the upgrade.

Next, we’ll retrieve the arguments to the Init call using the ChaincodeStubInterface.GetStringArgs function and check for validity. In our case, we are expecting a key-value pair.

Next, we’ll store the initial state in the ledger. To do this, we will call ChaincodeStubInterface.PutState with the key and value passed in as the arguments. Assuming all went well, return a peer.Response object that indicates the initialization was a success.

<pre class="file" data-filename="sacc.go">
// Init is called during chaincode instantiation to initialize any
// data. Note that chaincode upgrade also calls this function to reset
// or to migrate data, so be careful to avoid a scenario where you
// inadvertently clobber your ledger's data!
func (t *SimpleAsset) Init(stub shim.ChaincodeStubInterface) peer.Response {
  // Get the args from the transaction proposal
  args := stub.GetStringArgs()
  if len(args) != 2 {
    return shim.Error("Incorrect arguments. Expecting a key and a value")
  }

  // Set up any variables or assets here by calling stub.PutState()

  // We store the key and the value on the ledger
  err := stub.PutState(args[0], []byte(args[1]))
  if err != nil {
    return shim.Error(fmt.Sprintf("Failed to create asset: %s", args[0]))
  }
  return shim.Success(nil)
}
</pre>




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
`yes | ./byfn.sh generate`{{execute}}

You will see a brief description as to what will occur, along with a yes/no command line prompt. Respond with a y or hit the return key to execute the described action.

```
Generating certs and genesis block for channel 'mychannel' with CLI timeout of '10' seconds and CLI delay of '3' seconds
Continue? [Y/n] y
proceeding ...
/Users/xxx/dev/fabric-samples/bin/cryptogen
```

This first step generates all of the certificates and keys for our various network entities, the genesis block used to bootstrap the ordering service, and a collection of configuration transactions required to configure a Channel.