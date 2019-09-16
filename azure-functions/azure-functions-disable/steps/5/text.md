For scripting languages such as C# script and JavaScript, you use the disabled property of the function.json file to tell the runtime not to trigger a function. This property can be set to true or to the name of an app setting:

JSON

`
{
    "bindings": [
        {
            "type": "queueTrigger",
            "direction": "in",
            "name": "myQueueItem",
            "queueName": "myqueue-items",
            "connection":"MyStorageConnectionAppSetting"
        }
    ],
    "disabled": true
}
or

JSON

`
    "bindings": [
        ...
    ],
    "disabled": "IS_DISABLED"

In the second example, the function is disabled when there is an app setting that is named IS_DISABLED and is set to true or 1.