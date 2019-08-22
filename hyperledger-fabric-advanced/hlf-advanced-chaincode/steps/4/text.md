#### Terminal 2

**Note:** All command below will run in terminal 2 (It will open automatically on executing commands)

Now, move in the directory which contains scripts. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/peer/simple-two-org/ && chmod 755 *.sh`{{execute T2}}

Run following command to set the environment variables `. ./env.sh`{{execute T2}}

Also, run peer start command to start the peer. Also, check the log messages emitted by peer binary.
`peer node start`{{execute T2}}

#### Terminal 3

**Note:** All commands below will run in terminal 3 (It will open automatically on executing command)

Now, move in the directory which contains scripts. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/peer/simple-two-org/ && chmod 755 *.sh`{{execute T3}}

Run following command to set the environment variables in terminal 3.
`. ./env.sh`{{execute T3}}

#### Create Channel
You can Create the channel using the channel transaction created earlier
`peer channel create -o localhost:7050 -c acmechannel -f $CONFIG_DIRECTORY/acme-channel.tx`{{execute T3}}    

#### Join Channel
`peer channel join -o localhost:7050 -b ./acmechannel.block`{{execute T3}}    


