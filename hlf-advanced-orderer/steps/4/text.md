
In this step, we will look into pre-reqs that are needed to launch the orderer.



#### Setup cryptogen 
In the init.sh script, we will run following command to generate crypto material
```cryptogen generate --config=./crypto-config.yaml```

#### Setup the genesis block
In the init.sh script, we will run following command for writing genesis block
```configtxgen -profile AcmeOrdererGenesis -outputBlock ./acme-genesis.block -channelID ordererchannel```

#### reate the acmechannel transaction
In the init.sh script, we will run following command for writing acmechannel
```configtxgen -profile AcmeChannel -outputCreateChannelTx ./acme-channel.tx -channelID acmechannel```

Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../configtx/simple-two-org`{{copy}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

The genesis file is used for launching the orderer. Following configuration will be used to generate the genesis in the configtx.yaml file.

```
  AcmeOrdererGenesis:
      Orderer:
          <<: *OrdererDefaults
          Organizations:
              - *Orderer
      Consortiums:
          AirlineConsortium:
              Organizations:
                  - *Org1
```
