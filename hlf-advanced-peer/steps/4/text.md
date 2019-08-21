Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../cryptogen/simple-two-org`{{copy}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

You can generate the crypto material by calling: `cryptogen generate --help`{{copy}}

#### Validate
Validate that the crypto material was created for the organizations by going into the generated crypto-config DIRECTORY and then navigate to peerOrganizations. Explore the various directories



# Test commands for Peer 

#1 Terminal-1     Launch the Orderer
# PS: Setup the orderer before proceeding


`cd orderer/simple-two-org`{{execute T1}}

`./init.sh all`{{execute T1}}
`./launch.sh`{{execute T1}}

To experiment with recreation of the channel. Simply re-initialize 
the orderer and launch.

# Scripts
peer/simple-two-org
./clean.sh              Cleans up the ledger
./clean.sh  all         Cleans up the ledger and other network artefacts

.  env.sh               Sets the environment variables - always use with . as prefix
./show-env.sh           Shows the current environment setup for the peer

init.sh                 Initializes the peer setup
