**Note:** All command in this step will run in terminal 3 (It will open automatically on executing command)

Run following command to set the environment variables in terminal 3.
`env.sh`{{execute T3}}

You can create the channel using the channel transaction created earlier
`peer channel create -o localhost:7050 -c acmechannel -f $CONFIG_DIRECTORY/acme-channel.tx`{{execute T3}}    

Above command will generate the acmechannel.block. `ls`{{execute T3}}

#### Create Channel
You can Create the channel using the channel transaction created earlier
`peer channel create -o localhost:7050 -c acmechannel -f $CONFIG_DIRECTORY/acme-channel.tx`{{execute T3}}    

This will generate the acmechannel.block

#### Launch Peer
`peer node start -o localhost:7050`{{execute T3}}    

#### Join Channel
`peer channel join -o localhost:7050 -b ./acmechannel.block`{{execute T3}}    

#### List  Channels
`peer channel list`{{execute T3}}    

#### Fetch Channel
 `peer channel fetch 0 acmechannel.block -c acmechannel -o localhost:7050`{{execute T3}}    

