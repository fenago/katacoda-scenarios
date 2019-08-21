
Run following command to print the contents of a genesis block named acme-genesis.block to the screen as JSON.
`configtxgen -inspectBlock ./acme-genesis.block`{{copy}}

You can also store the result in the json file by running
`mkdir temp && configtxgen -inspectBlock ./acme-genesis.block > temp/acme-genesis.json`{{copy}}


```
Usage of configtxgen:
  -inspectBlock string
        Prints the configuration contained in the block at the specified path
```