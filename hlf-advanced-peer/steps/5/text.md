In this step, we will extend the organization by adding a new peer.  Do this by opening yaml file in Visual Studio Code by clicking in the vscode explorer: `crypto-config.addpeer.yaml`. It only contains the new peer information that you are adding.  


You can create the crypto for the new peer with:


#2 Terminal-2   Start the Peer
`env.sh`{{execute T2}}
`peer node start`{{execute T2}}


This is where we will check the log messages emitted by peer binary