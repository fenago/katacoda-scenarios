Functions are invoked by a trigger, such as an HTTP request, a timer, or an update to data. Your function needs to process that trigger, and any other inputs, to produce one or more outputs.

Use the Java annotations included in the **'com.microsoft.azure.functions.annotation.*'** package to bind input and outputs to your methods.

**Important:**
You must configure an Azure Storage account in your `local.settings.json` to run Azure Blob storage, Azure Queue storage, or Azure Table storage triggers locally.

Example:

```
public class Function {
    public String echo(@HttpTrigger(name = "req", 
      methods = {"post"},  authLevel = AuthorizationLevel.ANONYMOUS) 
        String req, ExecutionContext context) {
        return String.format(req);
    }
}
```
