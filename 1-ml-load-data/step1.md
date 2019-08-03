This is your first step

## Task

We need to load the Python Environment by running a **command**

`sudo apt update`{{execute}}
`sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget -y'{{execute}}
`wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz`{{execute}}
`tar -xf Python-3.7.3.tar.xz`{{execute}}
`cd Python-3.7.3`{{execute}}
`./configure --enable-optimizations`{{execute}}
`make -j 8`{{execute}}
`sudo make install`{{execute}}
`python3 --version`
