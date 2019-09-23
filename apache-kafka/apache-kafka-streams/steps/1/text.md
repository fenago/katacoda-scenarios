In this step, we will setup VScode editor and clone respository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/athertahir/kafka.git`{{execute}}

#### Permissions
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd kafka/setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh && cd ../Chapter06/kioto`{{execute T1}} 

**Note:**
The supplied commands in the next steps MUST be run from your `Chapter06/kioto` sub-directory of the **kafka** repository clone.


In this scenario, instead of using the Kafka Java API for producers and consumers as in previous chapters, we are going to use Kafka Streams, the Kafka module for stream processing.

- Kafka Streams in a nutshell
- Kafka Streams project setup
- Coding and running the Java `PlainStreamsProcessor`
- Scaling out with Kafka Streams
- Coding and running the Java `CustomStreamsProcessor`
- Coding and running the Java `AvroStreamsProcessor`
- Coding and running the Late `EventProducer`
- Coding and running the Kafka Streams processor