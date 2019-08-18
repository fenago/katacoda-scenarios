Building Your First Network
Note

In this step, we will clone fabric samples repository.

#### Clone fabric samples repository
`git clone https://github.com/hyperledger/fabric-samples.git`{{execute}}


Now, move in the directory into which you will install the Fabric Samples and binaries, go ahead and execute the command to pull down the binaries and images.
``cd fabric-samples && curl -sSL http://bit.ly/2ysbOFE | bash -s`{{execute}}


The build your first network (BYFN) scenario provisions a sample Hyperledger Fabric network consisting of two organizations, each maintaining two peer nodes. It also will deploy a “Solo” ordering service by default,though other ordering service implementations are available.

Install prerequisites
Before we begin, if you haven’t already done so, you may wish to check that you have all the Prerequisites installed on the platform(s) on which you’ll be developing blockchain applications and/or operating Hyperledger Fabric.

You will also need to Install Samples, Binaries and Docker Images. You will notice that there are a number of samples included in the fabric-samples repository. We will be using the first-network sample. Let’s open that sub-directory now.

`cd first-network`{{execute}}

**Note:**
The supplied commands in this documentation MUST be run from your first-network sub-directory of the fabric-samples repository clone. If you elect to run the commands from a different location, the various provided scripts will be unable to find the binaries.