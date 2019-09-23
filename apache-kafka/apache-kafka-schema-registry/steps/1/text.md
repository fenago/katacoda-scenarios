In this step, we will setup VScode editor and clone respository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/athertahir/kafka.git`{{execute}}

#### Permissions
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.

`cd kafka/setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh && cd ../Chapter05/kioto`{{execute T1}} 

**Note:**
The supplied commands in the next steps MUST be run from your `Chapter05/kioto` sub-directory of the **kafka** repository clone.


In this scenario, we will see how to serialize the messages with Apache Avro.

- Avro in a nutshell
- Defining the schema
- Using the Schema Registry
- How to build a Java `AvroProducer`, a consumer, and a processor
- How to run the Java `AvroProducer` and the processor