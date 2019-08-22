In this step, we will install all the Prerequisite i-e: doceker, docker-compose, golang and jq utility. 

1. Golang
2. Docker
3. Docker Compose
4. JQ Utility

#### Install Docker
Run `cat docker.sh`{{execute}} to view the contents of the bash script. Copy & execute `./docker.sh`{{execute}} command in the terminal to install docker and docker-compose.

You can verify docker is running on your System by running `docker version`{{execute}} command. Also, run `docker-compose version`{{execute}} to verify docker-compose.

#### Install Golang
Run `cat go.sh`{{execute}} to view the contents of the bash script. Copy & execute `./go.sh`{{execute}} command in the vscode terminal to install golang.

**Important** Run `source ~/.profile`{{execute}} to load golang path variables.

You can verify golang is installed on your System by running `go version`{{execute}} command.

#### Install JQ
Run `cat jq.sh`{{execute}} to view the contents of the bash script. Copy & execute `./jq.sh`{{execute}} command to install JQ utility.

You can verify jq is installed on your System by running `jq --version`{{execute}} command. you should get `jq-1.5-1-a5b5cbe` as output.