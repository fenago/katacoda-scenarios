
In this step, we will look into pre-reqs that are needed to launch the orderer.

#### Setup cryptogen 
In the init.sh script, we will run following command to generate crypto material
```cryptogen generate --config=./crypto-config.yaml```

#### Setup the genesis block
In the init.sh script, we will run following command for writing genesis block
```configtxgen -profile AcmeOrdererGenesis -outputBlock ./acme-genesis.block -channelID ordererchannel```

#### Create the acmechannel transaction
In the init.sh script, we will run following command for writing acmechannel
```configtxgen -profile AcmeChannel -outputCreateChannelTx ./acme-channel.tx -channelID acmechannel```

In the next step, we will setup these pre-reqs.