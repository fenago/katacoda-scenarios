Execute the following commands to install Java:

`apt-get update`{{execute}} 

`apt-get --assume-yes install default-jre`{{execute}} 

This command will install the Java Runtime Environment (JRE). This will allow you to run almost all Java software.

Verify the installation with: `java -version`{{execute}} 

You’ll see the following output:

```
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)
```

#### Install telnet
Execute the following command to install telnet:
`apt-get install telnet`{{execute}} 