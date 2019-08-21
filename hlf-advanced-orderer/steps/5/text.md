In this step, we will look into the contents of `orderer.yaml`.


#### Genesis Block
We have to specify genesis block in the orderer.yaml which we created using configtxgen utility. 

```
General:

    # Genesis Block Method = Provisional then GenesisProfile need to be specified 
    # GenesisMethod: provisional
    # GenesisProfile: AcmeOrdererGenesis

    # Genesis Block Method = file then GenesisFile need to be specified 
    # The genesis block file need to be generated using the configtxgen tool
    GenesisMethod: file
    GenesisFile: ./acme-genesis.block

```

#### LedgerType
Orderer supports following LedgerType:
1. Ram
2. Json or file
3. File

Filesystem type is used for production systems whereas ram or json can be for development.

```
    # Ledger Type can be ram, json or file
    LedgerType: file

```

We also have to specify Location in the orderer.yaml which will be used to store data by FileLedger. This applies to the configuration of the file or json ledgers

```
FileLedger:

    Location: /home/vagrant/ledgers/orderer/simple-two-orgs/ledger
    Prefix: hyperledger-fabric-ordererledger    
```

#### LocalMSPDir
Everything that interacts with a blockchain network, including peers, applications, admins, and orderers, acquires their organizational identity from their digital certificate and their Membership Service Provider (MSP) definition.

We will have to speecify directory for the private crypto material needed by the orderer created by cryptogen tool. 

```
    LocalMSPDir: ./crypto-config/ordererOrganizations/acme.com/orderers/orderer.acme.com/msp
```