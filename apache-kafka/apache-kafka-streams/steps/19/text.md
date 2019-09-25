To run the EventProcessor, follow these steps:

Create the aggregates topic as follows:
`~/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic aggregates --replication-factor 1 --partitions 4`{{execute T1}} 

Run a console consumer for the aggregates topic, as follows:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic aggregates --property print.key=true`{{execute T1}} 

#### Run EventProducer
Run the main method of the `EventProducer` in **terminal 2** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.events.EventProducer`{{execute T2}} 


#### Run EventProcessor
Run the main method of the `EventProcessor` in **terminal 3** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.events.EventProcessor`{{execute T3}} 

Remember that it writes to the topic every 30 seconds. The output on the console consumer for the aggregates topic should be similar to the following:

```
1532529050000 10
1532529060000 10
1532529070000 9
1532529080000 3
```

After the second window, we can see that the values in the KTable are updated with fresh (and correct) data, shown as follows:

```
1532529050000 10
1532529060000 10
1532529070000 10
1532529080000 10
1532529090000 10
1532529100000 4
```

Note how in the first print, the value for the last window is 3, and the window started in 1532529070000 has a value of 9. Then in the second print, the values are correct. This behavior is because in the first print, the delayed event had not arrived yet. When this finally arrived, the count values were corrected for all the windows.

 