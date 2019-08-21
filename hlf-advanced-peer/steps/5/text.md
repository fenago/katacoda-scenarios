**Note:** All command in this step will run in terminal 2 (It will open automatically on executing commands)

Now, move in the directory which contains scripts. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/peer/simple-two-org/ && chmod 755 *.sh`{{execute T2}}

Run following command to set the environment variables `. ./env.sh`{{execute T2}}

Also, run peer start command to start the peer. Also, check the log messages emitted by peer binary.
`peer node start`{{execute T2}}
