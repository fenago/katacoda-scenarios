To build the project, run this command from the kioto directory:
`gradle jar`{{execute T1}} 

If everything is okay, the output is something like the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
```


**Note:** 
- If above gradle command fails first time, you can try again.
- Following two commands will run in **terminal 2** (It will open automatically on executing command). 
- Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 2`.

#### Kafka topics
The broker is running on port 9092. To create the healthchecks topic, execute the following:
`~/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic healthchecks --replication-factor 1 --partitions 4`{{execute T2}} 


#### Kafka consumer
Run a console consumer for the healthchecks topic by typing the following:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic healthchecks`{{execute T2}} 


#### Run PlainProducer
Run the main method of the `PlainProducer` in **terminal 1** by running following command.
`java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainProducer`{{execute}} 


The output on the console consumer should be similar to the following:

```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2018-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}

{"event":"HEALTH_CHECK","factory":"Candelariohaven","serialNumber":"BO58-SB28","type":"SOLAR","status":"STARTING","lastStartedAt":"2018-08-16T04:00:00.179+0000","temperature":75.0,"ipAddress":"151.157.164.162"}

{"event":"HEALTH_CHECK","factory":"Ramonaview","serialNumber":"DV03-ZT93","type":"SOLAR","status":"RUNNING","lastStartedAt":"2018-07-12T10:16:39.091+0000","temperature":70.0,"ipAddress":"173.141.90.85"}
...
 
```

**Important** Press `Ctrl + C` in terminal **1** and **2** to quit programs before proceeding.


There is a trade-off among three factors: the availability to produce messages, the latency in the production, and the guarantee of the safe write.

In this example, we just have one broker, and we use the default value for acks of 1. When we call the get() method in the future, we are waiting for the broker acknowledgment, that is, we have a guarantee that the message is persisted before sending another message. In this configuration, we don't lose messages, but our latency is higher than in a fire and forget schema.