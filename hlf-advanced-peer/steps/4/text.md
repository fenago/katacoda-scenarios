Now, move in the directory which contains the sample `crypto-config.yaml` file `cd ../cryptogen/simple-two-org`{{execute T1}} and extend it to create the crypto for a new Organization.  Name the organization something unique (Not budget.com).  Use the existing Org as a template.

You can generate the crypto material by calling: `cryptogen generate --help`{{execute T1}}

#### Validate
Validate that the crypto material was created for the organizations by going into the generated crypto-config DIRECTORY and then navigate to peerOrganizations. Explore the various directories



# Test commands for Peer 

#1 Terminal-1     Launch the Orderer
# PS: Setup the orderer before proceeding


 In this step, we will launch the Orderer. Let's setup the orderer before proceeding. We also need to change permission to execute the script using **chmod**.

`cd ../orderer/simple-two-org && chmod 755 *.sh`{{execute T1}}

Let's first generate crypto material and channel tx
`./init.sh all`{{execute T1}}

Next, launch the orderer using bash script. We can do this by running
`./launch.sh`{{execute T1}}