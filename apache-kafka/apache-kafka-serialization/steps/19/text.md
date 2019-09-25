Run a console consumer in **terminal 1** for the uptimes topic as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T1}}


#### Run CustomProcessor
Run the main method of the `CustomProcessor` in **terminal 2** by running following command.
`cd ~/kafka/Chapter04/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.custom.CustomProcessor`{{execute T2}} 


#### Run CustomProducer
Run the main method of the `CustomProducer` in **terminal 3** by running following command.
`cd ~/kafka/Chapter04/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.custom.CustomProducer`{{execute T3}} 


The output on the console consumer **(terminal 1)** for the `uptimes` topic should be similar to the following:

```
EW05-HV36   33
BO58-SB28   20
DV03-ZT93   46
...
```

Now, we have seen how to create our own SerDe to abstract the serialization code from our application's main logic. Now you know how a Kafka SerDe works.