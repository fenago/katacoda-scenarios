The first step is to code our `Constants` class. This class is a static class with all of the Constants needed in our project.

Open the project with your favorite IDE and, under the src/main/java/kiotodirectory, open a file in **vscode** explorer called `Constants.java` with the content:

```
package kioto;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.databind.util.StdDateFormat;
public final class Constants {
  private static final ObjectMapper jsonMapper;
  static {
    ObjectMapper mapper = new ObjectMapper();
    mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
    mapper.setDateFormat(new StdDateFormat());
    jsonMapper = mapper;
  }
  public static String getHealthChecksTopic() {
    return "healthchecks";
  }
  public static String getHealthChecksAvroTopic() {
    return "healthchecks-avro";
  }
  public static String getUptimesTopic() {
    return "uptimes";
  }
  public enum machineType {GEOTHERMAL, HYDROELECTRIC, NUCLEAR, WIND, SOLAR}
  public enum machineStatus {STARTING, RUNNING, SHUTTING_DOWN, SHUT_DOWN}
  public static ObjectMapper getJsonMapper() {
    return jsonMapper;
  }
}
```

In our Constants class, there are some methods that we will need later. These are as follows:

- **getHealthChecksTopic:** It returns the name of the health checks input topic
- **getHealthChecksAvroTopic:** It returns the name of the topic with the health checks in Avro
- **getUptimesTopic:** It returns the name of the uptimes topic
- **machineType:** This is an enum with the types of the Kioto energy producing machines types
- **machineType:** This is an enum with the types of the Kioto machines' possible statuses
- **getJsonMapper:** It returns the object mapper for JSON serialization and we set the serialization format for dates

This is a `Constants` class; in languages such as Kotlin, the constants don't require an independent class, but we are using Java. Some purists of object-oriented programming argue that to code constant classes is an object-oriented anti-pattern. However, for simplicity here, we need some constants in our system.