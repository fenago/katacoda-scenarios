You see this output when the function is running locally on your system and ready to respond to HTTP requests:

#### Output
```
Listening on http://localhost:7071
Hit CTRL-C to exit...

Http Functions:

   hello: http://localhost:7071/api/HttpTrigger-Java
Trigger the function from the command line using curl in a new terminal window:
```

**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

#### CURL
`curl -w "\n" http://localhost:7071/api/HttpTrigger-Java -d LocalFunction`{{execute T2}}


```
Hello LocalFunction!
```

**Important:**
- Interface might keep switching back to terminal 1 because function app is running there after executing following command, you can manually switch by clicking `terminal 2`.
- Use `Ctrl` + `C` to stop the function app.
