In this step, we will learn peer chaincode command.

#### Install Code
`peer chaincode install -n gocc -v 1.0  -p chaincode_example02`{{execute T3}} 

#### Instantiate Code
`peer chaincode instantiate  -n gocc -v 1.0 -C acmechannel -c '{"Args":["init","a","100","b","200"]}'`{{execute T3}}

**Note:** Please wait for the few seconds for the above command to get response.

#### Check Status
`peer chaincode list  --installed`{{execute T3}}

`peer chaincode list  --instantiated   -C acmechannel`{{execute T3}}

#### Query & Invoke
`peer chaincode query -C acmechannel -n gocc  -c '{"Args":["query","a"]}'`{{execute T3}}

`peer chaincode invoke -C acmechannel -n gocc  -c '{"Args":["invoke","a","b","10"]}'`{{execute T3}}
