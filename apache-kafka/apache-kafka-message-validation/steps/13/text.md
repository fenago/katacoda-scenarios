The first step is open a `Validator.java` file in the src/main/java/monedero/ directory.


```
package monedero;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.clients.producer.KafkaProducer;
import java.io.IOException;

public class Validator implements Producer {
  private final KafkaProducer<String, String> producer;
  private final String validMessages;
  private final String invalidMessages;
  private static final ObjectMapper MAPPER = new ObjectMapper();

  public Validator(String servers, String validMessages, String invalidMessages) { //1
    this.producer = new KafkaProducer<>(Producer.createConfig(servers));
    this.validMessages = validMessages;
    this.invalidMessages = invalidMessages;
  }

  @Override
  public void process(String message) {
    try {
      JsonNode root = MAPPER.readTree(message);
      String error = "";
      error = error.concat(validate(root, "event")); //2
      error = error.concat(validate(root, "customer"));
      error = error.concat(validate(root, "currency"));
      error = error.concat(validate(root, "timestamp"));
      if (error.length() > 0) {
        Producer.write(this.producer, this.invalidMessages, //3
        "{\"error\": \" " + error + "\"}");
      } else {
        Producer.write(this.producer, this.validMessages, //4
        MAPPER.writeValueAsString(root));
      }
    } catch (IOException e) {
      Producer.write(this.producer, this.invalidMessages, "{\"error\": \""
      + e.getClass().getSimpleName() + ": " + e.getMessage() + "\"}");//5 
    }
  }
  private String validate(JsonNode root, String path) {
    if (!root.has(path)) {
      return path.concat(" is missing. ");
    }
    JsonNode node = root.path(path);
    if (node.isMissingNode()) {
      return path.concat(" is missing. ");
    }
    return "";
  }
}
```

As with Writer, the Validator class also implements the Producer class, but with the following:

- In line `//1`, its constructor takes two topics: the valid and the invalid-messages topic
- In line `//2`, the process method validates the fact that the message is in JSON format along with the existence of the fields: event, customer, currency, and timestamp
- In line `//3`, in case the message doesn't have any required field, an error message is sent to the invalid-messages topic
- In line `//4`, in case the message is valid, the message is sent to the valid-messages topic
- In line `//5`, in case the message is not in JSON format, an error message is sent to the invalid-messages topic