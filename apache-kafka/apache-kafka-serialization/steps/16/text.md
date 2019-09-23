
In a similar way, to build a custom deserializer, we need to create a class that implements the org.apache.kafka.common.serialization.Deserializer interface. We must indicate how to convert an array of bytes into a custom type (deserialization).

In the src/main/java/kioto/serde directory, Open a file called `HealthCheckDeserializer.java`:

```
package kioto.serde;
import kioto.Constants;
import kioto.HealthCheck;
import java.io.IOException;
import java.util.Map;
import org.apache.kafka.common.serialization.Deserializer;
public final class HealthCheckDeserializer implements Deserializer {
  @Override
  public HealthCheck deserialize(String topic, byte[] data) {
    if (data == null) {
      return null;
    }
    try {
      return Constants.getJsonMapper().readValue(data, HealthCheck.class);
    } catch (IOException e) {
      return null;
    }
  }
  @Override
  public void close() {}
  @Override
  public void configure(Map configs, boolean isKey) {}
}
```

Note that the deserializer class is located in a module called kafka-clients in the org.apache.kafka route. The objective here is to use the deserializer class instead of Jackson (manually).

Also note that the important method to implement is the deserialize method. The close and configure methods can be left with an empty body.

We import the HealthCheck class because the readValue method requires a POJO (a class with public constructor and public getters and setters). Note also that all of the POJO attributes should be serializables.