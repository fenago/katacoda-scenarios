
To add a function to your project, run the following command:
`func new`{{execute T1}}

Choose the HTTP trigger template, type HttpTrigger as the name for the function, then press Enter.

A subfolder named `HttpTrigger` is created, which contains the following files:

- **function.json:** configuration file that defines the function, trigger, and other bindings. Review this file and see that the value for scriptFile points to the file containing the function, while the invocation trigger and bindings are defined in the bindings array.

Each binding requires a direction, type and a unique name. The HTTP trigger has an input binding of type httpTrigger and output binding of type http.

- **__init__.py:** script file that is your HTTP triggered function. Review this script and see that it contains a default main(). HTTP data from the trigger is passed to this function using the req named binding parameter. Defined in function.json, req is an instance of the azure.functions.HttpRequest class.

The return object, defined as $return in function.json, is an instance of `azure.functions.HttpResponse` class.