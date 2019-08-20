The configtxgen command allows users to create and inspect channel config related artifacts. The content of the generated artifacts is dictated by the contents of configtx.yaml.

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{copy}} the command to download and install configtxgen utility.

#### Validate
You can verify configtxgen is installed on your System by running `configtxgen --version`{{copy}} command.

```
Usage of configtxgen:
  -asOrg string
        Performs the config generation as a particular organization (by name), only including values in the write set that org (likely) has privilege to set
  -channelCreateTxBaseProfile string
        Specifies a profile to consider as the orderer system channel current state to allow modification of non-application parameters during channel create tx generation. Only valid in conjuction with 'outputCreateChannelTx'.
  -channelID string
        The channel ID to use in the configtx
  -configPath string
        The path containing the configuration to use (if set)
  -inspectBlock string
        Prints the configuration contained in the block at the specified path
  -inspectChannelCreateTx string
        Prints the configuration contained in the transaction at the specified path
  -outputAnchorPeersUpdate string
        Creates an config update to update an anchor peer (works only with the default channel creation, and only for the first update)
  -outputBlock string
        The path to write the genesis block to (if set)
  -outputCreateChannelTx string
        The path to write a channel creation configtx to (if set)
  -printOrg string
        Prints the definition of an organization as JSON. (useful for adding an org to a channel manually)
  -profile string
        The profile from configtx.yaml to use for generation. (default "SampleInsecureSolo")
  -version
        Show version information
```

In the next steps, we will learn more configtxgen utility.

