
In this tutorial, We will use configtxgen utility for generating following:
1. Channel Tx
2. Anchor Peer Txn


#### Channel Tx
Channel Tx requires the following:
- Channel ID
- Configuration for the Application
- Configuration for the Consortiums


The following configuration will be used to generate the Channel Tx in the configtx.yaml file.
```
  AcmeChannel:
    Consortium: AirlineConsortium
    Application:
        <<: *ApplicationDefaults
        Organizations:
            - *Org1
```

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{copy}} the command to download and install configtxgen utility.

#### Validate
You can verify configtxgen is installed on your System by running `configtxgen --version`{{copy}} command.

#### Usage
Here’s some examples using the different available flags on the peer command `configtxgen --help`{{copy}}

We will use configtxgen utility for generating following:
1. Genesis Block
2. Channel Tx
3. Anchor Peer Txn

**Note**: configtxgen looks for at path `FABRIC_CFG_PATH` for `configtx.yaml`. If unset, the tool searches the current folder for the yaml file.