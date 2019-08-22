**Note:** All commands in this step will run in terminal 1.

In this step, we will launch the Orderer. Let's setup the orderer before proceeding. We also need to change permission to execute the script using **chmod**.

`cd ../orderer/simple-two-org && chmod 755 *.sh`{{execute T1}}

Let's first generate crypto material and channel tx
`./init.sh all`{{execute T1}}

Next, launch the orderer using bash script. We can do this by running
`./launch.sh`{{execute T1}}