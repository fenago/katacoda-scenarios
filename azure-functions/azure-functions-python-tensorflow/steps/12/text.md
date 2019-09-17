Open **classify/__init__.py** in your vscode editor. Import the predict library that you added to the same folder earlier. Add the following import statements below the other imports already in the file.


<pre class="file" data-target="clipboard">
import json
from .predict import predict_image_from_url
</pre>

Replace the function template code with the following.

<pre class="file" data-target="clipboard">
def main(req: func.HttpRequest) -> func.HttpResponse:
    image_url = req.params.get('img')
    results = predict_image_from_url(image_url)

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    return func.HttpResponse(json.dumps(results), headers = headers)
</pre>

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-python-tensorflow/steps/12/1.JPG)

This function receives an image URL in a query string parameter named img. It calls **predict_image_from_url** from the helper library that downloads the image and returns a prediction using the TensorFlow model. The function then returns an HTTP response with the results.

Since the HTTP endpoint is called by a web page hosted on another domain, the HTTP response includes an Access-Control-Allow-Origin header to satisfy the browser's Cross-Origin Resource Sharing (CORS) requirements.