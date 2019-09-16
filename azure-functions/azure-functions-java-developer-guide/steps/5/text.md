For local development of Java function apps, download and use the Azul Zulu Enterprise for Azure Java 8 JDKs from Azul Systems. Azure Functions uses the Azul Java 8 JDK runtime when you deploy your function apps to the cloud.

Azure support for issues with the JDKs and function apps is available with a qualified support plan.

#### Customize JVM
Functions lets you customize the Java virtual machine (JVM) used to run your Java functions. The following JVM options are used by default:

* -XX:+TieredCompilation
* -XX:TieredStopAtLevel=1
* -noverify
*-Djava.net.preferIPv4Stack=true
* -jar

You can provide additional arguments in an app setting named JAVA_OPTS. You can add app settings to your function app deployed to Azure in the Azure portal or the Azure CLI.