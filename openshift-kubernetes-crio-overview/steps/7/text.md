We mentioned earlier that CRI-O is using runc Container Runtime behind the scenes. To help us further with the verification process, we are going to use the runc command inside the Minikube VM. runc is a CLI command for running containers packaged according to the OCI format. The syntax of the runc command is very similar to the docker command we used in Chapter 1, Containers and Docker Overview.


`minikube ssh "sudo runc ps 3f2c2826318f1526bdb9710050a29b5d4a3de78d61e07ac9d83cedb9827c62e4"`{{execute}}

UID PID PPID C STIME TTY TIME CMD
root 5746 5695 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5788 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5792 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5793 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND


**Note:** that 3f2c2826318f1526bdb9710050a29b5d4a3de78d61e07ac9d83cedb9827c62e4 is the container ID from the kubectl describe pods/httpd-7dcb9bd6c4-x5dhm command we ran previously.