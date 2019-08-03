After (or as you are) following the lecture, complete these steps to get started.

## Task

We need to load the Python Environment by running these **commands**

###Update Ubuntu and provide the base packages
`sudo apt update`{{execute}}
`sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget -y`{{execute}}
###Download Python 3.7.3 and explode it
`wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz`{{execute}}
`tar -xf Python-3.7.3.tar.xz`{{execute}}
`cd Python-3.7.3`{{execute}}
`rm Python-3.7.3.tar.xz`{{execute}}
###Enable Optimizations and make python
`./configure --enable-optimizations`{{execute}}
`make -j 8`{{execute}}
`sudo make install`{{execute}}
`python3 --version`{{execute}}
