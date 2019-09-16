You can also use the Function State switch on the function's Manage tab. The switch works by creating and deleting the `AzureWebJobs.<FUNCTION_NAME>.Disabled` app setting.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-disable/steps/4/manage.JPG)

#### Functions 2.x - C# class libraries
In a Functions 2.x class library, we recommend that you use the method that works for all languages. But if you prefer, you can use the Disable attribute as in Functions `1.x`.