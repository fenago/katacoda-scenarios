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

To use Apache Spark, we need the dependency, shown as follows:

```
compile 'org.apache.spark:spark-sql_2.11:2.2.2'
```

To connect Apache Spark with Kafka, we need the dependency, shown as follows:

```
compile 'org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.2'
```
