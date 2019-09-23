To run the EventProducer, we follow these steps:

Create the events topic, as shown in the following block:
```
$. /bin/kafka-topics --zookeeper localhost:2181 --create --topic 
events --replication-factor 1 --partitions 4
Run a console consumer for the events topic using the following command:
```
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic events
From the IDE, run the main method of the EventProducer.
The output on the console consumer for the events topic should be similar to the following:
```
1532529060000,47, on time
1532529060000,48, on time
1532529060000,49, on time
1532529070000,50, on time
1532529070000,51, on time
1532529070000,52, on time
1532529070000,53, on time
1532529070000,55, on time
1532529070000,56, on time
1532529070000,57, on time
1532529070000,58, on time 
1532529070000,59, on time
1532529080000,0, on time
1532529080000,1, on time
1532529080000,2, on time
1532529080000,3, on time
1532529080000,4, on time
1532529080000,5, on time
1532529080000,6, on time
1532529070000,54, late
1532529080000,7, on time
...
Note that each event window changes every 10 seconds. Also, note how the 54th event is not sent between the 53rd and 55th events. The 54th event, belonging to a previous window, arrives in the next minute between the sixth and seventh seconds