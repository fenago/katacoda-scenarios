To build the project, run the following command from the kioto directory:

```
$ gradle jar
If everything is okay, the output is something like the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
Run a console consumer for HealthChecksTopic as follows:
```
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic healthchecks
From our IDE, run the main method of the CustomProducer
The output on the console consumer should be similar to the following:
```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2018-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}

{"event":"HEALTH_CHECK","factory":"Candelariohaven","serialNumber":"BO58-SB28","type":"SOLAR","status":"STARTING","lastStartedAt":"2018-08-16T04:00:00.179+0000","temperature":75.0,"ipAddress":"151.157.164.162"}

{"event":"HEALTH_CHECK","factory":"Ramonaview","serialNumber":"DV03-ZT93","type":"SOLAR","status":"RUNNING","lastStartedAt":"2018-07-12T10:16:39.091+0000","temperature":70.0,"ipAddress":"173.141.90.85"}

...