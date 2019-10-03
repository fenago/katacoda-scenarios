Task 3: Creating RDDs from Spark-Shell
Now that we have Spark installed in our machines. Let us begin coding with Spark. As a first step in our journey with Spark coding, let us look at the different ways to create an RDD. 


We need following packages to perform the lab exercise: 
- Java Development Kit
- SBT



#### JAVA
Verify the installation with: `java -version`{{execute}} 

You'll see the following output:

```
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)
```


#### Install SBT

**Step 1:** Run the following commands from the terminal to install sbt.

`echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list`{{execute}} 

`curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | apt-key add`{{execute}} 

`apt-get update`{{execute}} 

`apt-get install sbt`{{execute}} 


**Step 2:** Verify your Scala installation version by running the following command.
 
`sbt -version`{{execute}}

You will get following output.

```
Scala code runner version 2.12.8 -- Copyright 2002-2018, LAMP/EPFL and Lightbend, Inc.
```


