In this step, we will generate the anchor peer update tx which will be used by peers for submitting transaction.
`configtxgen -outputAnchorPeersUpdate ./Org1Anchors.tx -profile AcmeChannel -channelID acmechannel -asOrg Org1`{{copy}}

```
Usage of configtxgen:
  -asOrg string
        Performs the config generation as a particular organization (by name), only including values in the write set that org (likely) has privilege to set
  -channelID string
        The channel ID to use in the configtx
  -outputAnchorPeersUpdate string
        Creates an config update to update an anchor peer (works only with the default channel creation, and only for the first update)
  -profile string
        The profile from configtx.yaml to use for generation. (default "SampleInsecureSolo")
```

#### Verify
You can verify `Org1Anchors.tx` file was created by listing content of current directory `ls`{{copy}} command.