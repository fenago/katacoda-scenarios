
To open Application Insights from a function app in the Azure portal, go to the function app's Overview page. Under Configured features, select Application Insights.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/6/1.png)

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/6/2.png)


The following areas of Application Insights can be helpful when evaluating the behavior, performance, and errors in your functions:

Tab	| Description
--- | ---
`Failures` | 	Create charts and alerts based on function failures and server exceptions. The Operation Name is the function name. Failures in dependencies aren't shown unless you implement custom telemetry for dependencies.
`Performance` | 	Analyze performance issues.
`Servers` | 	View resource utilization and throughput per server. This data can be useful for debugging scenarios where functions are bogging down your underlying resources. Servers are referred to as Cloud role instances.
`Metrics` | 	Create charts and alerts that are based on metrics. Metrics include the number of function invocations, execution time, and success rates.
`Live Metrics Stream` | 	View metrics data as it's created in real time.