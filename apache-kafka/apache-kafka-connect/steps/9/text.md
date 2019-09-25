To build the project, run this command from the kioto directory:
`gradle build`{{execute}} 

If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 57s
5 actionable tasks: 5 executed
```

**Note:** If above command fails first time, you can try again.

Running the main method of the `PlainProducer` and console consumer for the uptimes topic. The output on the console consumer of the producer should be similar to the following:

```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2017-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}

{"event":"HEALTH_CHECK","factory":"Candelariohaven","serialNumber":"BO58-SB28","type":"SOLAR","status":"STARTING","lastStartedAt":"2017-08-16T04:00:00.179+0000","temperature":75.0,"ipAddress":"151.157.164.162"}

{"event":"HEALTH_CHECK","factory":"Ramonaview","serialNumber":"DV03-ZT93","type":"SOLAR","status":"RUNNING","lastStartedAt":"2017-07-12T10:16:39.091+0000","temperature":70.0,"ipAddress":"173.141.90.85"}
...
```

Running the main method of the `SparkProcessor` and console consumer for the uptimes topic. The output on the console consumer of the producer should be similar to the following:

```
      EW05-HV36   33
      BO58-SB28   20
      DV03-ZT93   46
      ...
```
