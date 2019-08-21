In this step, we will extend the organization by adding a new peer.  Do this by opening yaml file in Visual Studio Code by clicking in the vscode explorer: `crypto-config.addpeer.yaml`. It only contains the new peer information that you are adding.  


`env.sh`{{execute T3}}    

This is where we will execute the commands

Create the channel using the channel transaction created earlier
`peer channel create -o localhost:7050 -c acmechannel -f $CONFIG_DIRECTORY/acme-channel.tx`{{execute T3}}    

This will generate the acmechannel.block


Create the channel using the channel transaction created earlier

`peer channel create -o localhost:7050 -c acmechannel -f $CONFIG_DIRECTORY/acme-channel.tx`{{execute T3}}    

This will generate the acmechannel.block

Launch Peer
`peer node start -o localhost:7050`{{execute T3}}    

Join the channel

`peer channel join -o localhost:7050 -b ./acmechannel.block`{{execute T3}}    

List the channels

`peer channel list`{{execute T3}}    

fetch

 `peer channel fetch 0 acmechannel.block -c acmechannel -o localhost:7050`{{execute T3}}    

