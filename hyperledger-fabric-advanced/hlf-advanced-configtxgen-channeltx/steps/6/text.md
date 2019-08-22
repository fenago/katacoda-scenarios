Print the contents of a channel tx named acme-channel.tx to the screen as JSON.
`configtxgen -inspectChannelCreateTx ./acme-channel.tx`{{copy}}

You can also store the result in the json file by running
`mkdir -p temp && configtxgen -inspectChannelCreateTx ./acme-channel.tx > temp/acme-channel.json`{{copy}}

#### Usage

```
Usage of configtxgen:
  -inspectChannelCreateTx string
        Prints the configuration contained in the transaction at the specified path
```