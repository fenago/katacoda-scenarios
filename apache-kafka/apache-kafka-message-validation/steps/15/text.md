

To rebuild the project from the monedero directory, run the following command:
`gradle jar`{{execute T1}} 

If everything is OK, the output should be similar to the following:

```
...
BUILD SUCCESSFUL
...
```

To run the project, we need four different command-line windows. Following figure shows the command-line windows arrangement:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-validation/steps/15/1.jpg)

The four terminal windows to test the processing engine including: message producer, valid-message consumer, invalid-message consumer, and the processing engine itself