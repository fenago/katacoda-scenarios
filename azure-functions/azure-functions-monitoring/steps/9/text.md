In Node.js functions, use context.log to write logs. Structured logging isn't enabled.


```
context.log('JavaScript HTTP trigger function processed a request.' + context.invocationId);
```

#### Custom metrics logging
When you're running on version 1.x of the Functions runtime, Node.js functions can use the context.log.metric method to create custom metrics in Application Insights. This method isn't currently supported in version 2.x. Here's a sample method call:

```
context.log.metric("TestMetric", 1234);
```

This code is an alternative to calling trackMetric by using the Node.js SDK for Application Insights.