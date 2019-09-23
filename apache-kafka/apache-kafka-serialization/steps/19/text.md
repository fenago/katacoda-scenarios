To build the project, run the following command from the kioto directory:

```
$ gradle jar
If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
Run a console consumer for the uptimes topic as follows:
```
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic uptimes --property print.key=true
From our IDE, run the main method of CustomProcessor
From our IDE, run the main method of CustomProducer
The output on the console consumer for the uptimes topic should be similar to the following:
```
EW05-HV36   33
BO58-SB28   20
DV03-ZT93   46
...
Now, we have seen how to create our own SerDe to abstract the serialization code from our application's main logic. Now you know how a Kafka SerDe works.