We need following packages to perform the lab exercise: 
- Java Development Kit
- pyspark


#### JAVA
Verify the installation with: `java -version`{{execute T1}} 

You'll see the following output:

```
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)
```


#### Install pyspark
PySpark is available in pypi. To install just run `pip install pyspark`{{execute T1}} 

The Python packaging for Spark is not intended to replace all of the other use cases. This Python packaged version of Spark is suitable for interacting with an existing cluster (be it Spark standalone, YARN, or Mesos) - but does not contain the tools required to set up your own standalone Spark cluster.