Construct an organization definition based on the parameters such as MSPDir from configtx.yaml and print it as JSON to the screen. (This output is useful for channel reconfiguration workflows, such as adding a member).

`configtxgen -printOrg Org1`{{copy}}

You can also store the result in the json file by running
`mkdir -p temp && configtxgen -printOrg Org1 > temp/Org1.json`{{copy}}

```
Usage of configtxgen:
  -printOrg string
        Prints the definition of an organization as JSON. (useful for adding an org to a channel manually)
```