At the moment, the ProcessingEngine class coordinates the Reader and Writer classes. It contains the main method to coordinate them. We have to edit the ProcessingEngine class located in the src/main/java/monedero/ directory and change Writer with Validator, as in Listing 2.10.

The following is the content of Listing 2.10, ProcessingEngine.java:

```
package monedero;
public class ProcessingEngine {
  public static void main(String[] args) {
    String servers = args[0];
    String groupId = args[1];
    String inputTopic = args[2];
    String validTopic = args[3];
    String invalidTopic = args[4];
    Reader reader = new Reader(servers, groupId, inputTopic);
    Validator validator = new Validator(servers, validTopic, invalidTopic);
    reader.run(validator);
  }
}
```

ProcessingEngine receives five arguments from the command line:

- **args[0]:** servers, indicates the host and port of the Kafka broker
- **args[1]:** groupId, indicates that the consumer is part of this Kafka consumer group
- **args[2]:** inputTopic, the topic where Reader reads from
- **args[3]:** validTopic, the topic where valid messages are sent
- **args[4]:** invalidTopic, the topic where invalid messages are sent
 