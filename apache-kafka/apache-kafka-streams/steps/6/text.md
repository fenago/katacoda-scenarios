To build the project, run this command from the kioto directory:
`gradle build`{{execute T1}}

If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 1s
6 actionable task: 6 up-to-date
```

**Note:** If above command fails first time, you can try again.

The first step is to run a console consumer in **terminal 1** for the uptimes topic, shown in the following code snippet:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T1}}

**Note:**
- Interface will keep switching back to terminal 1 because consumer is running there after executing command, you can manually switch by clicking different terminal.
- Commands below will run in **terminal 2 & 3** respectively (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`


#### Run PlainStreamsProcessor
Run the main method of the `PlainStreamsProcessor` in **terminal 2** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainStreamsProcessor`{{execute T2}} 


#### Run PlainProducer
Run the main method of the `PlainProducer` in **terminal 3** by running following command.
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainProducer`{{execute T3}} 


**Important:** Press `Ctrl` + `C` in terminal 1, 2 & 3 to stop everything before proceeding to next step.


The output on the console consumer for the uptimes topic should be similar to the following:
```
EW05-HV36 33
BO58-SB28 20
DV03-ZT93 46
...
```
