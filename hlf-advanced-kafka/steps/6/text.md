
Let's first generate crypto material and channel tx
`./init.sh all`{{copy}}

You can verify init.sh was successfully was created by listing content of current directory `ls`{{copy}} command. Folowing files are created by above script.
```
acme-channel.tx  
acme-genesis.block
```

2. Publish a message
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TestTopic > /dev/null

3. Subscribe to a message
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic TestTopic --from-beginning
