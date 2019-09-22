The `ProcessingEngine` class coordinates the `Reader` and `Writer` classes. It contains the main method to coordinate them. Create a new file called `ProcessingEngine.java` in the src/main/java/monedero/directory and copy therein the code in Listing 2.8.

The following is the content of Listing 2.8, ProcessingEngine.java:

```
package monedero;
public class ProcessingEngine {
  public static void main(String[] args) {
    String servers = args[0];
    String groupId = args[1];
    String sourceTopic = args[2];
    String targetTopic = args[3];
    Reader reader = new Reader(servers, groupId, sourceTopic);
    Writer writer = new Writer(servers, targetTopic);
    reader.run(writer);
  }
}
```

ProcessingEngine receives four arguments from the command line:

- **args[0]:** servers, the host and port of the Kafka broker
- **args[1]:** groupId, the consumer group of the consumer
- **args[2]:** sourceTopic, inputTopic where Reader reads from
- **args[3]:** targetTopic, outputTopic where Writer writes to