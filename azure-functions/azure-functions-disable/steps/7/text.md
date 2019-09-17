In a Functions 1.x class library, you use a Disable attribute to prevent a function from being triggered. You can use the attribute without a constructor parameter, as shown in the following example:

```
public static class QueueFunctions
{
    [Disable]
    [FunctionName("QueueTrigger")]
    public static void QueueTrigger(
        [QueueTrigger("myqueue-items")] string myQueueItem, 
        TraceWriter log)
    {
        log.Info($"C# function processed: {myQueueItem}");
    }
}
```

The attribute without a constructor parameter requires that you recompile and redeploy the project to change the function's disabled state. A more flexible way to use the attribute is to include a constructor parameter that refers to a Boolean app setting, as shown in the following example:

```
public static class QueueFunctions
{
    [Disable("MY_TIMER_DISABLED")]
    [FunctionName("QueueTrigger")]
    public static void QueueTrigger(
        [QueueTrigger("myqueue-items")] string myQueueItem, 
        TraceWriter log)
    {
        log.Info($"C# function processed: {myQueueItem}");
    }
}
```

This method lets you enable and disable the function by changing the app setting, without recompiling or redeploying. Changing an app setting causes the function app to restart, so the disabled state change is recognized immediately.

**Important:**
The Disabled attribute is the only way to disable a class library function. The generated function.json file for a class library function is not meant to be edited directly. If you edit that file, whatever you do to the disabled property will have no effect.

The same goes for the **Function state** switch on the **Manage** tab, since it works by changing the function.json file.