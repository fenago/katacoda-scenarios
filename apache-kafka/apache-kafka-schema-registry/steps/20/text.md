Running the AvroProcessor
To build the project, run the following command from the kioto directory:

Copy
$ gradle jar
If everything is correct, the output will be something like this:

Copy
BUILD SUCCESSFUL in 3s
 1 actionable task: 1 executed
Run a console consumer for the uptimes topic, as shown here:

Copy
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic uptimes --property print.key=true
From the IDE, run the main method of the AvroProcessor
From the IDE, run the main method of the AvroProducer
The output on the console consumer for the uptimes topic should be similar to this:
Copy
EW05-HV36 33
BO58-SB28 20
DV03-ZT93 46
...