Execute the following commands to install Java:

`apt-get update`{{execute}} 

`apt-get --assume-yes install default-jre`{{execute}} 

This command will install the Java Runtime Environment (JRE). This will allow you to run almost all Java software.

Verify the installation with: java -version

You’ll see the following output:

```
openjdk version "10.0.1" 2018-04-17
OpenJDK Runtime Environment (build 10.0.1+10-Ubuntu-3ubuntu1)
OpenJDK 64-Bit Server VM (build 10.0.1+10-Ubuntu-3ubuntu1, mixed mode)
```

#### Install telnet
Execute the following command to install telnet:
`apt-get install telnet`{{execute}} 