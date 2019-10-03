Task 1: 
**Step 1:** From the terminal, run the following commands to install JDK (Java Development Kit).

`sudo apt-get update`{{execute}} 

This will update the package index. You might be asked to enter your password after you run the command above. 

**Step 2:** Once you run the above command, run the following command to actually download and install JDK.

`sudo apt-get install default-jdk`{{execute}} 


Verify the installation with: `java -version`{{execute}} 

You’ll see the following output:

```
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)
```
