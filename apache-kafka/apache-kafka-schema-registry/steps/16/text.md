
Running the AvroProducer
To build the project, run the following command from the kioto directory:

Copy
$ gradle jar
If everything is OK, the output is something like the one shown here:

Copy
BUILD SUCCESSFUL in 3s
 1 actionable task: 1 executed


The broker is running on port 9092. To create the healthchecks-avro topic, execute the following command:
Copy
$ ./bin/kafka-topics --zookeeper localhost:2181 --create --topic healthchecks-avro --replication-factor 1 --partitions 4
Note that we are just creating a normal topic and nothing indicates the messages' format.
Run a console consumer for the healthchecks-avro topic:
Copy
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic healthchecks-avro