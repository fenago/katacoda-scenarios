You can verify the libraries we wish to use, that is, requests and urllib, either from the command line or by importing the Python IDE and getting details on the package using the help() method:

`pip install requests`{{execute}}

```
Requirement already satisfied: requests in c:\python37\lib\site-packages (2.19.1)
```

As shown in the preceding code, we are trying to install requests, but the command returns Requirement already satisfied. The pip command checks for an existing installation on the system before installing a fresh library. 

In the following code block, we will be using the Python IDE to import urllib. We'll view its details using Python's built-in help() method.

`python`{{execute}}

The `>>>` symbol in code represents use of the Python IDE; it accepts the code or instructions and displays the output on the next line:


`import urllib`{{execute}}

`help(urllib) #display documentation available for urllib`{{execute}}

Execute `q`{{execute}} to exit help menu. 

Similar to the previous code, lets import requests using the Python IDE:

`import requests`{{execute}}

`requests.__version__ #display requests version`{{execute}}

`help(requests)   #display documentation available for requests`{{execute}}

Execute `q`{{execute}} to exit help menu. 

If we import urllib or requests and these libraries don't exist, the result will throw an error:

```
ModuleNotFoundError: No module named 'requests'
```

You can also upgrade the module version using the --upgrade argument:
`pip install requests -–upgrade`