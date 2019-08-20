Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../cryptogen/simple-two-org`{{copy}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

You can generate the crypto material by calling: `cryptogen generate --help`{{copy}}

#### Validate
Validate that the crypto material was created for the organizations by going into the generated crypto-config DIRECTORY and then navigate to peerOrganizations. Explore the various directories