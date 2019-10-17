
In order to install the Operator we need to make sure kubectl binary is installed on your machine. You can download the latest release with the command:

```curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl```{{execute}}

Then, make the kubectl binary executable.
`chmod +x ./kubectl`{{execute}}

Move the binary in to your PATH.
`sudo mv ./kubectl /usr/local/bin/kubectl`{{execute}}

And finally test to ensure the version you installed is up-to-date:
`kubectl version`{{execute}}

```
Client Version: version.Info{Major:"1", Minor:"15", GitVersion:"v1.15.3", GitCommit:"2d3c76f9091b6bec110a5e63777c332469e0cba2", GitTreeState:"clean", BuildDate:"2019-08-19T11:13:54Z", GoVersion:"go1.12.9", Compiler:"gc", Platform:"linux/amd64"}
```
