
We’ll leverage the CLI container to drive the calls.
`docker exec -it cli bash`{{execute T3}}

`peer chaincode install -p chaincodedev/chaincode/sacc -n mycc -v 0`{{execute T3}}

`peer chaincode instantiate -n mycc -v 0 -c '{"Args":["a","10"]}' -C myc`{{execute T3}}

#### Testing chaincode
Run followng chaincode query CLI command to get the value of a.
`peer chaincode query -n mycc -c '{"Args":["query","a"]}' -C myc`{{execute T3}}