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