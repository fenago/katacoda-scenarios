Azure Functions offers built-in integration with Azure Application Insights to monitor functions. This article shows you how to configure Azure Functions to send system-generated log files to Application Insights.

It is recommend to use **Application Insights** because it collects `log`, `performance`, and `error` data. It automatically detects performance anomalies and includes powerful analytics tools to help you diagnose issues and to understand how your functions are used. It's designed to help you continuously improve performance and usability.

As the required Application Insights instrumentation is built into Azure Functions, all you need is a valid instrumentation key to connect your function app to an Application Insights resource