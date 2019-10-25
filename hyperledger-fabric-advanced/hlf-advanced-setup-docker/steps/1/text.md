In this step, we will setup VScode editor and clone repository.


Let's run an instance of an **ubuntu** image and pass `/bin/bash`{{copy}} as argument to docker run command. We will also mount docker.sock to make docker from ther container.
`docker run -v /var/run/docker.sock:/var/run/docker.sock -ti --name hlf ubuntu /bin/bash`{{execute}}

- It runs a bare-bones, no-frills ubuntu system.
- -i tells Docker to connect us to the container's stdin.
- -t tells Docker that we want a pseudo-terminal

**Note:** If ubuntu is not present locally, you will also see a few extra lines, corresponding to the download of the ubuntu image.

# Task 
Now, we will install a package in our ubuntu container. We want git, so let's install it:
`apt-get update && apt-get install -y git`{{execute}}

Next, clone the following repository by executing following command in the container shell.
`git clone https://github.com/fenago/HLFADV.git`{{execute}}

#### Permissions
Now, move in the directory which contains scripts to install all the prerequisites and the Fabric Samples and binaries, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/setup && chmod 755 *.sh`{{execute}}