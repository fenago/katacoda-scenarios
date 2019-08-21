Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../configtx/simple-two-org`{{copy}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

The genesis file is used for launching the orderer. Following configuration will be used to generate the genesis in the configtx.yaml file.

Let's first generate crypto config using cryptogen utility
`cryptogen generate --config=../../cryptogen/simple-two-org/crypto-config.yaml`{{copy}}

#### Validate
Validate that the crypto material was created for the organizations by verifying that generated crypto-config directory was generated `ls`{{copy}}