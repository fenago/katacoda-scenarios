To rebuild the project from the monedero directory, run the following command:

gradle jar
 

If everything is OK, the output should be similar to the following:

```
...
BUILD SUCCESSFUL in 8s
2 actionable tasks: 2 executed
```

To run the project, we need four different command-line windows. Figure 3.3 shows the command-line windows arrangement:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-enrichment/steps/12/1.jpg)

The four terminal windows to test the processing engine including: message producer, valid message consumer, invalid message consumer, and the processing engine itself