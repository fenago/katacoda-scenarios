Maven will ask you for values needed to finish generating the project. For groupId, artifactId, and version values, see the Maven naming conventions reference. The appName value must be unique across Azure, so Maven generates an app name based on the previously entered artifactId as a default. The packageName value determines the Java package for the generated function code.

The `com.fabrikam.functions` and `fabrikam-functions` identifiers below are used as an example and to make later steps in this quickstart easier to read.

**groupId**: `com.fabrikam.functions`{copy}}
**artifactId**: `fabrikam-functions`{copy}}

```
Define value for property 'groupId' (should match expression '[A-Za-z0-9_\-\.]+'): com.fabrikam.functions
Define value for property 'artifactId' (should match expression '[A-Za-z0-9_\-\.]+'): fabrikam-functions
Define value for property 'version' 1.0-SNAPSHOT : 
Define value for property 'package': com.fabrikam.functions
Define value for property 'appName' fabrikam-functions-20170927220323382:
Define value for property 'appRegion' westus: :
Define value for property 'resourceGroup' java-functions-group: :
Confirm properties configuration: Y
```


