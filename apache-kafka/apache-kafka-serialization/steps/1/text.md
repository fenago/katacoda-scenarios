In this step, we will setup VScode editor and clone respository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/athertahir/kafka.git`{{copy}}

#### Permissions
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh`{{execute T1}} 

**Note:**
The supplied commands in the next steps MUST be run from your setup/kafka sub-directory of the **HLFADV** repository clone.



In modern (internet) computing, we often forget that entities must be transmitted from one computer to another. In order to be able to transmit the entities, they must first be serialized.

Serialization is the process of transforming an object into a stream of bytes commonly used to transmit it from one computer to another.

Deserialization, as the name implies, is the opposite of serialization, that is, to convert a stream of bytes into an object (for didactic purposes, we can say that the object is inflated or rehydrated), normally from the side that receives the message. Kafka provides Serializer/Deserializer (SerDe) for the primitive data types (byte, integer, long, double, String, and so on).

In this chapter, a new company is introduced: Kioto (standing for Kafka Internet of Things). This chapter covers the following topics:

- How to build a Java PlainProducer, a consumer, and a processor
- How to run a Java PlainProducer and a processor
- How to build a custom serializer and a custom deserializer
- How to build a Java CustomProducer, a consumer, and a processor
- How to run a Java CustomProducer and a processor