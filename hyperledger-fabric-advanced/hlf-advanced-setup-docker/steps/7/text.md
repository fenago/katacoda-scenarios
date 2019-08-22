Let's run an instance of an **hlf-custom** image and pass `/bin/bash`{{copy}} as argument to docker run command. We will also mount docker.sock to make docker from ther container.
`docker run -v /var/run/docker.sock:/var/run/docker.sock -ti --name hlf hlf-custom /bin/bash`{{execute}}

#### Validate
You can verify our changes are saved by running following commands. import was successful by running following commands.
`jq --version`{{execute}} 

`go version`{{execute}}

`orderer version`{{execute}}

`peer version`{{execute}}

`fabric-ca-server version`{{execute}}

`fabric-ca-client version`{{execute}}
