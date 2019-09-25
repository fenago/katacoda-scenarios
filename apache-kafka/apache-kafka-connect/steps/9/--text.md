To build the project, run this command from the kioto directory:
`gradle build`{{execute}} 

If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
```

**Note:** If above command fails first time, you can try again.

#### Kafka Consumer
Run a console consumer for the uptimes topic, shown as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes`{{execute}} 

#### Running PlainProducer
Run the main method of the `PlainProducer` in **terminal 2** by running following command.
`cd ~/kafka/Chapter08/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainProducer`{{execute T2}} 


#### Output
The output on the console consumer of the producer should be similar to the following:
```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2017-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}

{"event":"HEALTH_CHECK","factory":"Candelariohaven","serialNumber":"BO58-SB28","type":"SOLAR","status":"STARTING","lastStartedAt":"2017-08-16T04:00:00.179+0000","temperature":75.0,"ipAddress":"151.157.164.162"}

{"event":"HEALTH_CHECK","factory":"Ramonaview","serialNumber":"DV03-ZT93","type":"SOLAR","status":"RUNNING","lastStartedAt":"2017-07-12T10:16:39.091+0000","temperature":70.0,"ipAddress":"173.141.90.85"}
...
```

#### Running SparkProcessor
Run the main method of the `SparkProcessor` in **terminal 3** by running following command.
`cd ~/kafka/Chapter08/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.spark.SparkProcessor`{{execute T3}} 

#### Output
The output on the console consumer for the uptimes topic should be similar to the following:
```
      EW05-HV36   33
      BO58-SB28   20
      DV03-ZT93   46
      ...
```
