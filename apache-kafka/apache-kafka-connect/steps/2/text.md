Kafka Connect is an open source framework, part of Apache Kafka; it is used to connect Kafka with other systems, such as structured databases, column stores, key-value stores, filesystems, and search engines. 

Kafka Connect has a wide range of built-in connectors. If we are reading from the external system, it is called a data source; if we are writing to the external system, it is called a data sink.

```
{"event":"HEALTH_CHECK","factory":"Lake Anyaport","serialNumber":"EW05-HV36","type":"WIND","status":"STARTING","lastStartedAt":"2018-09-17T11:05:26.094+0000","temperature":62.0,"ipAddress":"15.185.195.90"}
...
```
we are going to process this data to calculate the machine's uptime and to obtain a topic with messages like these three:

```
EW05-HV36   33
BO58-SB28   20
DV03-ZT93   46
```