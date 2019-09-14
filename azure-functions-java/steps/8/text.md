You see this output when the function is running locally on your system and ready to respond to HTTP requests:

## Output

```
Listening on http://localhost:7071
Hit CTRL-C to exit...

Http Functions:

   hello: http://localhost:7071/api/HttpTrigger-Java
Trigger the function from the command line using curl in a new terminal window:
```

## CMD

`curl -w "\n" http://localhost:7071/api/HttpTrigger-Java -d LocalFunction`{{execute T1}}

## Output

```
Hello LocalFunction!
```

Use `Ctrl` + `C` in the terminal to stop the function code.