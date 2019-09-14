The following command starts the function app, which runs locally using the same Azure Functions runtime that is in Azure.

console

`
func host start
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

Content root path: C:\functions\MyFunctionProj
Now listening on: http://0.0.0.0:7071
Application started. Press Ctrl+C to shut down.

...

Http Functions:

        HttpTrigger: http://localhost:7071/api/HttpTrigger

[8/27/2018 10:38:27 PM] Host started (29486ms)
[8/27/2018 10:38:27 PM] Job host started
```

**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

`curl http://localhost:7071/api/HttpTrigger?name=Azure`{{execute T2}}

The function should execute and return **Hello Azure!**. Interface will switch back to terminal 1 after executing above command, you can manually click terminal 2 to see response.

**Important:** Use `Ctrl` + `C` to stop the function app.