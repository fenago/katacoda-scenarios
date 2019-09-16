Ensure the Python virtual environment is still activated and start the function app using the following command.

`func start`{{execute T1}}

In a browser, open this URL that calls your function with the URL of a cat photo. Confirm that a valid prediction result is returned.

```curl http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/Azure-Samples/functions-python-tensorflow-tutorial/master/resources/assets/samples/cat1.png```{{execute T2}}

You will get following response:
```
{"created": "2019-09-14T15:47:34.949519", "predictedTagName": "cat", "prediction": [{"tagName": "cat", "probability": 1.0}]}
```

**Note:**: Interface will switch back to terminal 1 after executing above command, you can manually click terminal 2 to see response.

Keep the function app running.