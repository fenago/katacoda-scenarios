In this step, we will setup VScode editor and clone repository.

Clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/athertahir/kafka.git`{{execute}}

#### Permissions
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd kafka/setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh && cd ../Chapter06/kioto`{{execute T1}} 

**Note:**
- The supplied commands in the next steps MUST be run from your `Chapter06/kioto` sub-directory of the **kafka** repository clone.
- Final code was already cloned from github for this scenario. You can just understand the application code in the next steps and run it using the instructions.
- Click **IDE Editor** tab to open Visual Studio and select explorer as show below:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/1.JPG)


In this scenario, instead of using the Kafka Java API for producers and consumers as in previous chapters, we are going to use Kafka Streams, the Kafka module for stream processing.

- Kafka Streams in a nutshell
- Kafka Streams project setup
- Coding and running the Java `PlainStreamsProcessor`
- Scaling out with Kafka Streams
- Coding and running the Java `CustomStreamsProcessor`
- Coding and running the Java `AvroStreamsProcessor`
- Coding and running the Late `EventProducer`
- Coding and running the Kafka Streams processor