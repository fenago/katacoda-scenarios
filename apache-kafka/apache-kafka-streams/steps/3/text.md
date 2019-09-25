
We are going to build our project with Gradle. The first step is to download and install Gradle from http://www.gradle.org/downloads.

Gradle only requires a Java JDK (version 7 or higher).

Linux users can install Gradle with the apt-get command, as follows:

`apt-get update`{{execute T1}} 
 
`yes | apt-get install gradle`{{execute T1}} 

`gradle -v`{{execute T1}} 

The output is something like the following:

```
------------------------------------------------------------
Gradle 4.10.2
------------------------------------------------------------
```


For the examples in this scenario, we also need the dependencies for Jackson. To use Kafka Streams, we just need one dependency, which is given in the following code snippet:

```
compile 'org.apache.kafka:kafka-streams:2.0.0'
```

To use Apache Avro with Kafka Streams, we add the serializers and deserializers as given in the following code:

```
compile 'io.confluent:kafka-streams-avro-serde:5.0.0'
```

The following lines are needed to run a Kafka Streams application as a jar. The build generates a fat jar:

```
configurations.compile.collect {
  it.isDirectory() ? it : zipTree(it)
}
```

The directory tree structure of the project should be as follows:

```
src
main
--java
----kioto
------avro
------custom
------events
------plain
------serde
--resources
test
```
