When you configure the Allowed origins list for your function app, the Access-Control-Allow-Origin header is automatically added to all responses from HTTP endpoints in your function app.

Configure function app's CORS list

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-manage/steps/9/cors.JPG)


When the wildcard `(*)` is used, all other domains are ignored.

Use the az functionapp cors add command to add a domain to the allowed origins list. The following example adds the `contoso.com` domain:

```az functionapp cors add --name <FUNCTION_APP_NAME> \
--resource-group <RESOURCE_GROUP_NAME> \
--allowed-origins https://contoso.com```{{copy}}

Use the az functionapp cors show command to list the current allowed origins.