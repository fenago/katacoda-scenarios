To build the project, run this command from the kioto directory as follows:

```
$ gradle jar
If everything is OK, the output is something similar to the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
```

#### Kafka Consumer
Run a console consumer for the uptimes topic, shown as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes`{{execute}} 

#### Running PlainProducer
From our IDE, run the main method of the PlainProducer built in previous chapters

The output on the console consumer of the producer should be similar to the following:
```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2017-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}
{"event":"HEALTH_CHECK","factory":"Candelariohaven","serialNumber":"BO58-SB28","type":"SOLAR","status":"STARTING","lastStartedAt":"2017-08-16T04:00:00.179+0000","temperature":75.0,"ipAddress":"151.157.164.162"}
{"event":"HEALTH_CHECK","factory":"Ramonaview","serialNumber":"DV03-ZT93","type":"SOLAR","status":"RUNNING","lastStartedAt":"2017-07-12T10:16:39.091+0000","temperature":70.0,"ipAddress":"173.141.90.85"}
...
```

#### Running SparkProcessor
From our IDE, run the main method of the SparkProcessor

#### Output
The output on the console consumer for the uptimes topic should be similar to the following:
```
      EW05-HV36   33
      BO58-SB28   20
      DV03-ZT93   46
      ...
```
