The following command starts the function app, which runs locally using the same Azure Functions runtime that is in Azure.

`func host start`{{execute}} 

When the Functions host starts, it writes something like the following output, which has been truncated for readability:

```
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

Content root path: /home/scrapbook/tutorial/MyFunctionProj
Now listening on: http://0.0.0.0:7071
Application started. Press Ctrl+C to shut down.

...

Http Functions:

        HttpTrigger: http://localhost:7071/api/HttpTrigger

[09/18/2019 10:03:32] Host started (29486ms)
[09/18/2019 10:03:32] Job host started
```

We will test this powershell function using `cURL` in the next step.