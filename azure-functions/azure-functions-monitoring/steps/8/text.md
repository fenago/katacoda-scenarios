You can use Application Insights without any custom configuration. The default configuration can result in high volumes of data. If you're using a Visual Studio Azure subscription, you might hit your data cap for Application Insights. Later in this article, you learn how to configure and customize the data that your functions send to Application Insights. For a function app, logging is configured in the host.json file.

#### Categories
The Azure Functions logger includes a category for every log. The category indicates which part of the runtime code or your function code wrote the log.

The Functions runtime creates logs with a category that begin with "Host." In version 1.x, the function started, function executed, and function completed logs have the category Host.Executor. Starting in version 2.x, these logs have the category Function.<YOUR_FUNCTION_NAME>.

If you write logs in your function code, the category is Function in version 1.x of the Functions runtime. In version 2.x, the category is Function.<YOUR_FUNCTION_NAME>.User.

#### Log levels
The Azure Functions logger also includes a log level with every log. LogLevel is an enumeration, and the integer code indicates relative importance:

LogLevel |	Code
--- | --- 
`Trace`      | 	0
`Debug`      | 	1
`Information`| 	2
`Warning`    | 	3
`Error`      |  4 
`Critical`   | 	5
`None`       | 	6

**Log configuration in host.json**
The `host.json` file configures how much logging a function app sends to Application Insights. For each category, you indicate the minimum log level to send. There are two examples: the first example targets the Functions version 2.x runtime (.NET Core) and the second example is for the version 1.x runtime.

#### Version 2.x
The v2.x runtime uses the .NET Core logging filter hierarchy.

```
{
  "logging": {
    "fileLoggingMode": "always",
    "logLevel": {
      "default": "Information",
      "Host.Results": "Error",
      "Function": "Error",
      "Host.Aggregator": "Trace"
    }
  }
}
```

#### Version 1.x
```
{
  "logger": {
    "categoryFilter": {
      "defaultLevel": "Information",
      "categoryLevels": {
        "Host.Results": "Error",
        "Function": "Error",
        "Host.Aggregator": "Trace"
      }
    }
  }
}
```

This example sets up the following rules:

- For logs with category Host.Results or Function, send only Error level and above to Application Insights. Logs for Warning level and below are ignored.
- For logs with category Host.Aggregator, send all logs to Application Insights. The Trace log level is the same as what some loggers call Verbose, but use Trace in the host.json file.
- For all other logs, send only Information level and above to Application Insights.


The category value in host.json controls logging for all categories that begin with the same value. Host in host.json controls logging for Host.General, Host.Executor, Host.Results, and so on.

If host.json includes multiple categories that start with the same string, the longer ones are matched first. Suppose you want everything from the runtime except Host.Aggregator to log at Error level, but you want Host.Aggregator to log at the Information level:

Version 2.x

```
{
  "logging": {
    "fileLoggingMode": "always",
    "logLevel": {
      "default": "Information",
      "Host": "Error",
      "Function": "Error",
      "Host.Aggregator": "Information"
    }
  }
}
```

#### Version 1.x

```
{
  "logger": {
    "categoryFilter": {
      "defaultLevel": "Information",
      "categoryLevels": {
        "Host": "Error",
        "Function": "Error",
        "Host.Aggregator": "Information"
      }
    }
  }
}
```

To suppress all logs for a category, you can use log level None. No logs are written with that category and there's no log level above it.