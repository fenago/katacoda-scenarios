In this step, we will clone fabric samples repository.
`git clone https://github.com/hyperledger/fabric-samples.git`{{execute}}


#### Install prerequisites
Before we begin, let's install all the Prerequisites on the platform(s) on which you’ll be developing blockchain applications and/or operating Hyperledger Fabric.

Now, move in the directory into which you will install the Fabric Samples and binaries, go ahead and execute the command to pull down the binaries and images.
`cd fabric-samples && curl -sSL http://bit.ly/2ysbOFE | bash -s`{{execute}}

**Note:** Please wait for the above script to complete, It will take around 3 minutes to complete.

The build your first network (BYFN) scenario provisions a sample Hyperledger Fabric network consisting of two organizations, each maintaining two peer nodes. It also will deploy a “Solo” ordering service by default,though other ordering service implementations are available.

You will notice that there are a number of samples included in the fabric-samples repository. We will be using the first-network sample. Let’s open that sub-directory now.

`cd first-network`{{execute}}

**Note:**
The supplied commands in this documentation MUST be run from your first-network sub-directory of the fabric-samples repository clone. If you elect to run the commands from a different location, the various provided scripts will be unable to find the binaries.