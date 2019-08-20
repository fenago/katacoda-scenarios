Print an organization definition
Construct an organization definition based on the parameters such as MSPDir from configtx.yaml and print it as JSON to the screen. (This output is useful for channel reconfiguration workflows, such as adding a member).

`configtxgen -printOrg Org1`{{copy}}

You can also store the result in the json file by running
`mkdir -p temp && configtxgen -printOrg Org1 > temp/Org1.json`{{copy}}

Let's first generate crypto config using cryptogen utility
`cryptogen generate --config=../../cryptogen/simple-two-org/crypto-config.yaml`{{copy}}

In this step, we will write a genesis block for channel ordererchannel for profile AcmeOrdererGenesis.
`export FABRIC_CFG_PATH=$PWD`{{copy}}

`configtxgen -profile AcmeOrdererGenesis -channelID ordererchannel -outputBlock acme-genesis.block`{{copy}}

#### Verify
You can verify genesis block was created by listing content of current directory `ls`{{copy}} command.


```
Usage of configtxgen:
  -channelID string
        The channel ID to use in the configtx
  -outputBlock string
        The path to write the genesis block to (if set)
  -profile string
        The profile from configtx.yaml to use for generation. (default "SampleInsecureSolo")
```
