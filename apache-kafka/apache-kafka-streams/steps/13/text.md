To build the project, run this command from the kioto directory:
`gradle build`{{execute}} 

If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 1s
 6 actionable task: 6 up-to-date
```

**Note:** If above command fails first time, you can try again.

The first step is to run a console consumer for the uptimes topic, shown as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092  --topic uptimes --property print.key=true`{{execute T1}} 


#### Run AvroStreamsProcessor
Run the main method of the `AvroStreamsProcessor` in **terminal 2** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.avro.AvroStreamsProcessor`{{execute T2}} 

#### Run AvroProducer
Run the main method of the `AvroProducer` in **terminal 3** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.avro.AvroProducer`{{execute T3}} 

The output on the console consumer for the uptimes topic should be similar to the following:
```
       EW05-HV36 33
       BO58-SB28 20
       DV03-ZT93 46
       ...
```
