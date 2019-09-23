We are going to build our project with Gradle. The first step is to download and install Gradle.

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


**Note:** Final code was already cloned from github for this scenario. You can just understand the application design and run it using the instructions.


The following content is of the Kioto Gradle build file:

```
apply plugin: 'java'
apply plugin: 'application'
sourceCompatibility = '1.8'
mainClassName = 'kioto.ProcessingEngine'
repositories {
    mavenCentral()
    maven { url 'https://packages.confluent.io/maven/' }
}
version = '0.1.0'
dependencies {
    compile 'com.github.javafaker:javafaker:0.15'
    compile 'com.fasterxml.jackson.core:jackson-core:2.9.7'
    compile 'io.confluent:kafka-avro-serializer:5.0.0'
    compile 'org.apache.kafka:kafka_2.12:2.0.0'
}
jar {
    manifest {
        attributes 'Main-Class': mainClassName
    } from {
        configurations.compile.collect {
            it.isDirectory() ? it : zipTree(it)
        }
    }
    exclude "META-INF/*.SF"
    exclude "META-INF/*.DSA"
    exclude "META-INF/*.RSA"
}
```

Some library dependencies added to the application are as follows:

- **kafka_2.12**, the necessary dependencies for Apache Kafka
- **javafaker**, the necessary dependencies for JavaFaker
- **jackson-core**, for JSON parsing and manipulation
- **kafka-avro-serializer**, to serialize in Kafka with Apache Avro