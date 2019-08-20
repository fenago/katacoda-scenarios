Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../configtx/simple-two-org`{{copy}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

The genesis file is used for launching the orderer. Following configuration will be used to generate the genesis in the configtx.yaml file.

Let's first generate crypto config using cryptogen utility
`cryptogen generate --config=../../cryptogen/simple-two-org/crypto-config.yaml`{{copy}}

In this step, we will write a genesis block which will be used for launching the orderer.
`export FABRIC_CFG_PATH=$PWD`{{copy}}

`configtxgen -profile AcmeOrdererGenesis -channelID ordererchannel -outputBlock acme-genesis.block`{{copy}}

#### Verify
You can verify genesis block was created by listing content of current directory `ls`{{copy}} command.

The Tx file is used by peers for submitting transaction.

```
Usage of configtxgen:
  -channelID string
        The channel ID to use in the configtx
  -outputCreateChannelTx string
        The path to write a channel creation configtx to (if set)
  -profile string
        The profile from configtx.yaml to use for generation. (default "SampleInsecureSolo")

```

# 3. 
configtxgen -outputCreateChannelTx ./acme-channel.tx  -profile AcmeChannel -channelID acmechannel
