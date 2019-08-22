
In this tutorial, We will use configtxgen utility for generating Channel Tx.

Channel Tx requires the following:
- Channel ID
- Configuration for the Application
- Configuration for the Consortiums

The following configuration will be used to generate the Channel Tx in the configtx.yaml file.
```
  AcmeChannel:
    Consortium: AirlineConsortium
    Application:
        <<: *ApplicationDefaults
        Organizations:
            - *Org1
```
