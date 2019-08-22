Run following command`cat fabric-setup.sh`{{execute}} to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{execute}} the command to pull down the binaries and images.

**Note:** Please wait for the above command to complete, It will take few seconds to complete.

#### Validate
You can verify fabric setup was successful by listing contents of the directory is running on Your System by running `cd ../fabric-samples && ls -la && cd ../setup`{{execute}} command.

It will create the folders under the current directory
    - fabric-samples

You can also verify setup was successful by running following commands on your System.
`orderer version`{{execute}}

`peer version`{{execute}}

**Note:** Please wait for the above script to complete, It will take around 2 minutes to complete.