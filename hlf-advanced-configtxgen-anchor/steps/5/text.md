Print the contents of a channel creation tx named create_chan_tx.pb to the screen as JSON.
`configtxgen -inspectChannelCreateTx ./Org1Anchors.tx`{{copy}}

You can also store the result in the json file by running
`mkdir -p temp && configtxgen -inspectChannelCreateTx ./Org1Anchors.tx > temp/updatepeers.json`{{copy}}

```
Usage of configtxgen:
  -inspectChannelCreateTx string
        Prints the configuration contained in the transaction at the specified path
```