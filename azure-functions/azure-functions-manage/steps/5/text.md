The function app settings values can also be read in your code as environment variables. 

#### Environment variables
In Functions, app settings, such as service connection strings, are exposed as environment variables during execution. You can access these settings by using `System.getenv("AzureWebJobsStorage")`.

The following example gets the application setting, with the key named myAppSetting:

#### Java

```
public class Function {
    public String echo(@HttpTrigger(name = "req", methods = {"post"}, authLevel = AuthorizationLevel.ANONYMOUS) String req, ExecutionContext context) {
        context.getLogger().info("My app setting value: "+ System.getenv("myAppSetting"));
        return String.format(req);
    }
}
```

When you develop a function app locally, you must maintain local copies of these values in the local.settings.json project file. To learn more, see Local settings file.