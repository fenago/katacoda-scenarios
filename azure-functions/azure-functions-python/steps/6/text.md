Run the function locally
The following command starts the function app, which runs locally using the same Azure Functions runtime that is in Azure.

console

`
func host start
When the Functions host starts, it writes something like the following output, which has been truncated for readability:

output

`

                  %%%%%%
                 %%%%%%
            @   %%%%%%    @
          @@   %%%%%%      @@
       @@@    %%%%%%%%%%%    @@@
     @@      %%%%%%%%%%        @@
       @@         %%%%       @@
         @@      %%%       @@
           @@    %%      @@
                %%
                %

...

Content root path: C:\functions\MyFunctionProj
Now listening on: http://0.0.0.0:7071
Application started. Press Ctrl+C to shut down.

...

Http Functions:

        HttpTrigger: http://localhost:7071/api/HttpTrigger

[8/27/2018 10:38:27 PM] Host started (29486ms)
[8/27/2018 10:38:27 PM] Job host started
` the URL of your HttpTrigger function from the runtime output and paste it into your browser's address bar. Append the query string ?name=<yourname> to this URL and execute the request. The following shows the response in the browser to the GET request returned by the local function: