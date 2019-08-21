In this step, we will extend the organization by adding a new peer.  Do this by opening yaml file in Visual Studio Code by clicking in the vscode explorer: `crypto-config.addpeer.yaml`. It only contains the new peer information that you are adding.  


Install the test code

`peer chaincode install -n gocc -v 1.0  -p chaincode_example02`{{execute T3}} 

Instantiate the code

`peer chaincode instantiate  -n gocc -v 1.0 -C acmechannel -c '{"Args":["init","a","100","b","200"]}'`{{execute T3}}

Check Status

`peer chaincode list  --installed`{{execute T3}}
`peer chaincode list  --instantiated   -C acmechannel`{{execute T3}}

Query & invoke

`peer chaincode query -C acmechannel -n gocc  -c '{"Args":["query","a"]}'`{{execute T3}}
`peer chaincode invoke -C acmechannel -n gocc  -c '{"Args":["invoke","a","b","10"]}'`{{execute T3}}
