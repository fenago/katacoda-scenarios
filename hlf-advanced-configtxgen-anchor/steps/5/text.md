In this step, we will generate the anchor peer update tx which will be used by peers for submitting transaction.
`configtxgen -outputAnchorPeersUpdate ./Org1Anchors.tx -profile AcmeChannel -channelID acmechannel -asOrg Org1`{{copy}}

```
Usage of configtxgen:
  -channelID string
        The channel ID to use in the configtx
  -outputCreateChannelTx string
        The path to write a channel creation configtx to (if set)
  -profile string
        The profile from configtx.yaml to use for generation. (default "SampleInsecureSolo")

```

#### Verify
You can verify `Org1Anchors.tx` file was created by listing content of current directory `ls`{{copy}} command.