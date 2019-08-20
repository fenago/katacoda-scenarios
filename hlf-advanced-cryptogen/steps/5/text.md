In this step, we will extend the organization by adding a new peer.  Do this by opening yaml file in Visual Studio Code by clicking in the vscode explorer: `crypto-config.addpeer.yaml`. It only contains the new peer information that you are adding.  

```
# Extends the crypto material for the setup
# Adds a new peer for Org1

#### Peers for acme
PeerOrgs:
  # Peer configuration for ACME
  - Name: Org1
    Domain: acme.com
    Specs:
      - Hostname: devpeer2
        CommonName: devpeer2
```

You can reate the crypto for the new peer with:
`cryptogen extend --help`{{copy}}
