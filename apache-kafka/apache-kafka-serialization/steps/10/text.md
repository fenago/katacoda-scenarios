To build the project, run the following command from the kioto directory:

Copy
$ gradle jar
 

 

If everything is correct, the output is something like the following:

Copy
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
Our broker is running on port 9092, so to create the uptimes topic, execute the following command:
Copy
$ ./bin/kafka-topics --zookeeper localhost:2181 --create --topic 
uptimes --replication-factor 1 --partitions 4
Run a console consumer for the uptimes topic, as follows:
Copy
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic uptimes --property print.key=true
