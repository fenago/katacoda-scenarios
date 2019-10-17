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

`apt-get install sbt && sbt sbtVersion > /dev/null 2>&1`{{execute}} 

**Step 2:** Verify your sbt installation version by running the following command.	

`sbt sbtVersion`{{execute}}	

You will get following output.

```	
[info] Loading project definition from /home/scrapbook/tutorial/apache-spark/project	
[info] Loading settings for project apache-spark from build.sbt ...	
[info] Set current project to Spark (in build file:/home/scrapbook/tutorial/apache-spark/)	
[info] 1.3.2
```

**Note:** If you get an error first time, please run the command again.