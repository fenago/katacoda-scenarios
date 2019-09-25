So far, we have seen how to produce and consume JSON messages using plain Java and Jackson. We will see here how to create our custom serializers and deserializers.

We have seen how to use `StringSerializer` in the producer and `StringDeserializer` in the consumer. Now, we will see how to build our own SerDe to abstract the serialization/deserialization processes away from the core code of the application.

To build a custom serializer, we need to create a class that implements the org.apache.kafka.common.serialization.Serializer interface. This is a generic type, so we can indicate the custom type to be converted into an array of bytes (serialization).

In the src/main/java/kioto/serdedirectory, open a file in **vscode** explorer called HealthCheckSerializer.java with the content of Listing 4.11.

The following is the content of Listing 4.11, HealthCheckSerializer.java: 

```
package kioto.serde;
import com.fasterxml.jackson.core.JsonProcessingException;
import kioto.Constants;
import java.util.Map;
import org.apache.kafka.common.serialization.Serializer;
public final class HealthCheckSerializer implements Serializer {
  @Override
  public byte[] serialize(String topic, Object data) {
    if (data == null) {
      return null;
    }
    try {
      return Constants.getJsonMapper().writeValueAsBytes(data);
    } catch (JsonProcessingException e) {
      return null;
    }
  }

  @Override
  public void close() {}
  @Override
  public void configure(Map configs, boolean isKey) {}
}
```

Note that the serializer class is located in a special module called kafka-clients in the org.apache.kafka route. The objective here is to use the serializer class instead of Jackson (manually).

Also note that the important method to implement is the serialize method. The close and configure methods can be left with an empty body.

We import the `JsonProcessingException` of Jackson just because the `writeValueAsBytes` method throws this exception, but we don't use Jackson for serialization.