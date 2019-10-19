At the time of writing, there is no distributed version of the Mask R-CNN library, so we have to install it
manually. The good news is that this is very easy. Installation involves cloning the GitHub
repository and running the installation script on your workstation. If you are having trouble,
see the installation instructions in the library’s readme file.

#### Step 1. Clone the Mask R-CNN GitHub Repository
This is as simple as running the following command from your command line:
`git clone https://github.com/matterport/Mask_RCNN.git`{{execute}} 

This will create a new local directory with the name `Mask_RCNN`.


#### Step 2. Install the Mask R-CNN Library
The library can be installed directly via pip. Change directory into the Mask RCNN project
directory and run the installation script. From the command line, type the following:


`apt-get update`{{execute}} 

`apt-get install -y python`{{execute}} 

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py`{{execute}} 

`cd Mask_RCNN`{{execute}} 

`python setup.py install && cd ..`{{execute}} 

The library will then install directly and you will see a lot of successful installation messages
ending with the following:

```
...
Finished processing dependencies for mask-rcnn==2.1
```

This confirms that you installed the library successfully and that you have the latest version,
which at the time of writing is version 2.1.

#### Step 3: Confirm the Library Was Installed
It is always a good idea to confirm that the library was installed correctly. You can confirm
that the library was installed correctly by querying it via the pip command; for example:

`pip show mask-rcnn`{{execute}} 


You should see output informing you of the version and installation location; for example:

```
Name: mask-rcnn
Version: 2.1
Summary: Mask R-CNN for object detection and instance segmentation
Home-page: https://github.com/matterport/Mask_RCNN
Author: Matterport
Author-email: waleed.abdulla@gmail.com
License: MIT
Location: ...
Requires:
Required-by:
```

We are now ready to use the library.