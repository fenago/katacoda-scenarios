To build the project, run the following command from the kioto directory:
`gradle jar`{{execute}} 

If everything is correct, the output will be something like this:

```
BUILD SUCCESSFUL in 3s
 1 actionable task: 1 executed
```

Run a console consumer in **terminal 1** for the uptimes topic, as shown here:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T1}} 

#### Run AvroProcessor
Run the main method of the `AvroProcessor` in **terminal 2** by running following command.
`cd ~/kafka/Chapter05/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.avro.AvroProcessor`{{execute T2}} 


#### Run AvroProducer
Run the main method of the `AvroProducer` in **terminal 3** by running following command.
`cd ~/kafka/Chapter05/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.avro.AvroProducer`{{execute T3}} 


The output on the console consumer for the uptimes topic should be similar to this:
```
EW05-HV36 33
BO58-SB28 20
DV03-ZT93 46
...
```
