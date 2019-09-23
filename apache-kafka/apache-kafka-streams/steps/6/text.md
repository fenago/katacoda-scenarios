To build the project, run this command from the kioto directory:

```
$ gradle build
If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 1s
6 actionable task: 6 up-to-date
The first step is to run a console consumer for the uptimes topic, shown in the following code snippet:
```
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic uptimes --property print.key=true
From the IDE, run the main method of the PlainStreamsProcessor
From the IDE, run the main method of the PlainProducer (built in previous chapters)
The output on the console consumer for the uptimes topic should be similar to the following:
```
EW05-HV36 33
BO58-SB28 20
DV03-ZT93 46
...