Ensure the Python virtual environment is still activated and start the function app using the following command.

`func start`{{execute T1}}

In a browser, open this URL that calls your function with the URL of a cat photo. Confirm that a valid prediction result is returned.

```http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/Azure-Samples/functions-python-tensorflow-tutorial/master/resources/assets/samples/cat1.png```{{execute T1}}

Keep the function app running.