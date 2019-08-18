Invoking the Chaincode
First, let’s add the Invoke function’s signature.

```
// Invoke is called per transaction on the chaincode. Each transaction is
// either a 'get' or a 'set' on the asset created by Init function. The 'set'
// method may create a new asset by specifying a new key-value pair.
func (t *SimpleAsset) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
}
```

As with the Init function, we need to extract the arguments from the ChaincodeStubInterface. The Invoke function’s arguments will be the name of the chaincode application function to invoke. In our case, our application will simply have two functions: set and get, that allow the value of an asset to be set or its current state to be retrieved. We first call ChaincodeStubInterface.GetFunctionAndParameters to extract the function name and the parameters to that chaincode application function.

Next, we’ll validate the function name as being either set or get, and invoke those chaincode application functions, returning an appropriate response via the shim.Success or shim.Error functions that will serialize the response into a gRPC protobuf message.

<pre class="file" data-filename="sacc.go">
// Invoke is called per transaction on the chaincode. Each transaction is
// either a 'get' or a 'set' on the asset created by Init function. The Set
// method may create a new asset by specifying a new key-value pair.
func (t *SimpleAsset) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
    // Extract the function and args from the transaction proposal
    fn, args := stub.GetFunctionAndParameters()

    var result string
    var err error
    if fn == "set" {
            result, err = set(stub, args)
    } else {
            result, err = get(stub, args)
    }
    if err != nil {
            return shim.Error(err.Error())
    }

    // Return the result as success payload
    return shim.Success([]byte(result))
}
</pre>


Next, you can bring the network up with one of the following commands:
`./byfn.sh up`{{execute}}

You will be prompted as to whether you wish to continue or abort. Respond with a y or hit the return key

The above command will compile Golang chaincode images and spin up the corresponding containers. Go is the default chaincode language, however there is also support for Node.js and Java chaincode. If you’d like to run through this tutorial with node chaincode, pass the following command instead:

```
# we use the -l flag to specify the chaincode language
# forgoing the -l flag will default to Golang

./byfn.sh up -l node
```

Тo make the sample run with Java chaincode, you have to specify -l java as follows:
```
./byfn.sh up -l java
```

**Caution:** Do not run both of these commands. Only one language can be tried unless you bring down and recreate the network between.

**Note:**