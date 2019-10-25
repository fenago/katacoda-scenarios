In this step, we will setup VScode editor and clone repository.

Click **IDE Editor** tab to open Visual Studio and click explorer.

Clone the following repository by copying & executing following command.
`git clone https://github.com/athertahir/kafka.git`{{execute}}

#### Install Kafka/Zookeeper
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd kafka/setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh`{{execute T1}} 
