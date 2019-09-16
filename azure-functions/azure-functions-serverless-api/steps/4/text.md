Next, test your function to see it working with the new API surface.

1. Navigate back to the development page by clicking on the function's name in the left navigation.
2. Click Get function URL and copy the URL. You should see that it uses the /api/hello route now.
3. Copy the URL into a new browser tab or your preferred REST client. Browsers will use GET by default.
4. Add parameters to the query string in your URL e.g. `/api/hello/?name=John`
5. Hit 'Enter' to confirm that it is working. You should see the response "Hello John"
6. You can also try calling the endpoint with another HTTP method to confirm that the function is not executed. For this,you will need to use a REST client, such as cURL, Postman, or Fiddler.