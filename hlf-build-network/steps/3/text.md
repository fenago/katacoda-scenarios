Next, you can bring the network up with one of the following commands:
`./byfn.sh up`{{execute}}

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


To connect to a validator node running on the Libra testnet, run the client as shown below.	Since the client is connected to a node on the testnet, you will see the following output.
`./scripts/cli/start_cli_testnet.sh`{{execute}}	

This command builds and runs the client utilizing cargo (Rust’s package manager) and connects the client to a validator node on the testnet.	

Once the client connects to a node on the testnet, you will see the following output.

```
usage: <command> <args>

Use the following commands:
...

Please, input commands:

libra%
```

**Note:** You can verify CLI Client Is Running on Your System by running `help`{{execute}} command. you should get 
**"connected to the validator"** as output.