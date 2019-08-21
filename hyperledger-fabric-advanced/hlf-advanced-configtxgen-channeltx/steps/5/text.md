In this step, we will create a Tx file which will be used by peers for submitting transaction.
`configtxgen -outputCreateChannelTx ./acme-channel.tx  -profile AcmeChannel -channelID acmechannel`{{copy}}

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
You can verify Tx file was created by listing content of current directory `ls`{{copy}} command.