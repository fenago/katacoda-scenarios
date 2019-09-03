Geth, also known as Go Ethereum, is the most popular Ethereum implementation that allows you to do a wide variety of tasks. We will go through how to do most of them in the following sections to help you understand how to execute each of the commands that are required for every task.

Building Geth (command line client)
Clone the repository to a directory of your choosing:

git clone https://github.com/ethereum/go-ethereum
Install latest distribution of Go if you don't have it already.

Building geth requires Go and C compilers to be installed:

sudo apt-get install -y build-essential
Finally, build the geth program using the following command.

cd go-ethereum
make geth
You can now run build/bin/geth to start your node.