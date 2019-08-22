Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../configtx/simple-two-org`{{copy}} in vscode **terminal** and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

The genesis file is used for launching the orderer. Following configuration will be used to generate the genesis in the configtx.yaml file.

```
  AcmeOrdererGenesis:
      Orderer:
          <<: *OrdererDefaults
          Organizations:
              - *Orderer
      Consortiums:
          AirlineConsortium:
              Organizations:
                  - *Org1
```
