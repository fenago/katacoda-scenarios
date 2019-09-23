Run a console consumer for the uptimes topic as follows:

`~/kafka/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T1}}


#### Run CustomProcessor
Run the main method of the `CustomProcessor` in **terminal 2** by running following command.
`java -cp ./build/libs/kioto-0.1.0.jar kioto.custom.CustomProcessor`{{execute T2}} 


#### Run CustomProducer
Run the main method of the `CustomProducer` in **terminal 3** by running following command.
`java -cp ./build/libs/kioto-0.1.0.jar kioto.custom.CustomProducer`{{execute T3}} 



From our IDE, run the main method of CustomProcessor
From our IDE, run the main method of CustomProducer

The output on the console consumer for the uptimes topic should be similar to the following:

```
EW05-HV36   33
BO58-SB28   20
DV03-ZT93   46
...
```

Now, we have seen how to create our own SerDe to abstract the serialization code from our application's main logic. Now you know how a Kafka SerDe works.