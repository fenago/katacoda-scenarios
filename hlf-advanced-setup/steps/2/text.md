In this step, we will install all the Prerequisite i-e: doceker, docker-compose, golang and jq utility. 

1. Golang
2. Docker
3. Docker Compose
4. JQ Utility

#### Install Docker
Open `docker.sh` to view the contents of the bash script. Copy & execute `./docker.sh`{{copy}} command in the vscode terminal to install and docker-compose.

You can verify docker is running on your System by running `docker version`{{copy}} command. Also, run `docker version`{{copy}}  to verify docker-compose.

#### Install Golang
Open `go.sh` to view the contents of the bash script. Copy & execute `./go.sh`{{copy}} command in the vscode terminal to install and docker-compose.


#### Install JQ
Open `jq.sh` to view the contents of the bash script. Copy & execute `./jq.sh`{{copy}} command to install and docker-compose.

You can verify jq is installed on your System by running `jq --version`{{copy}} command. you should get `jq-1.5-1-a5b5cbe` as output.

Let's install all the Prerequisites on the platform(s) on which you’ll be developing blockchain applications and/or operating Hyperledger Fabric.


Open `docker.sh` to view the contents of the bash script. Copy & execute  command to pull down the binaries and images.

5. Fabric Binaries and Samples




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
`./byfn.sh generate`{{copy}}

You will see a brief description as to what will occur, along with a yes/no command line prompt. Respond with a y or hit the return key to execute the described action.

```
Generating certs and genesis block for channel 'mychannel' with CLI timeout of '10' seconds and CLI delay of '3' seconds
Continue? [Y/n] y
proceeding ...
/Users/xxx/dev/fabric-samples/bin/cryptogen
```

This first step generates all of the certificates and keys for our various network entities, the genesis block used to bootstrap the ordering service, and a collection of configuration transactions required to configure a Channel.