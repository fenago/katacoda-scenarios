Now, we should modify our Java Producer to send messages in Avro format. First, it is important to mention that in Avro there are two types of messages:

Specific records: The file with the Avro schema (avsc) is sent to a specific Avro command to generate the corresponding Java classes.
Generic records: In this approach, a data structure similar to a map dictionary is used. This means that you set and get the fields by their names and you must know their corresponding types. This option is not type-safe, but it offers much more flexibility than the other, and here the versions are much easier to manage over time. In this example, we will use this approach.
Before we start with the code, remember that in the last chapter we added the library to support Avro to our Kafka client. If you recall, the build.gradle file has a special repository with all this libraries.

Confluent's repository is specified in the following line:

```
repositories {
 ...
 maven { url 'https://packages.confluent.io/maven/' }
 }
```

In the dependencies section, we should add the specific Avro libraries:

```
dependencies {
 ...
 compile 'io.confluent:kafka-avro-serializer:5.0.0'
 }
```

Do not use the libraries provided by Apache Avro, because they will not work. As we already know, to build a Kafka message producer, we use the Java client library; in particular, the producer API. As we already know, there are two requisites that all the Kafka producers should have: to be a KafkaProducer and to set the specific Properties, such as Listing 5.3:

```
import io.confluent.kafka.serializers.KafkaAvroSerializer; 
import org.apache.avro.Schema;
import org.apache.avro.Schema.Parser;
import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.common.serialization.StringSerializer;

public final class AvroProducer {
  private final Producer<String, GenericRecord> producer; //1
  private Schema schema;

  public AvroProducer(String brokers, String schemaRegistryUrl) { //2
    Properties props = new Properties();
    props.put("bootstrap.servers", brokers);
    props.put("key.serializer", StringSerializer.class); //3
    props.put("value.serializer", KafkaAvroSerializer.class); //4
    props.put("schema.registry.url", schemaRegistryUrl) //5
    producer = new KafkaProducer<>(props);

    try {
      schema = (new Parser()).parse( new 
      File("src/main/resources/healthcheck.avsc")); //6
    } catch (IOException e) {
      // deal with the Exception
    }
  }
  ...
}
```

An analysis of the AvroProducer constructor shows the following:

- In line `//1`, the values now are of type org.apache.avro.generic.GenericRecord
- In line `//2`, the constructor now receives the Schema Registry URL
- In line `//3`, the Serializer type for the messages' keys remains as StringSerializer
- In line `//4`, the Serializer type for the messages' values now is a KafkaAvroSerializer
- In line `//5`, the Schema Registry URL is added to the Producer properties
- In line `//6`, the avsc file with the schema definition is parsed with a Schema Parser

Because we have chosen the use of generic records, we have to load the schema. Note that we could have obtained the schema from the Schema Registry, but this is not safe because we do not know which version of the schema is registered. Instead of this, it is a smart and safe practice to store the schema along with the code. In this way, our code will always produce the correct data types, even when someone else changes the schema registered in the Schema Registry.