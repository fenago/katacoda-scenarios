Run the following command from the command line to create a function app project in the MyFunctionProj folder of the current local directory. 
`func init MyFunctionProj --docker`{{execute}}

When prompted, select a worker runtime **node** > **typescript** from the following language choices:

- **dotnet** 
- **node** 
- **python** 
- **powershell** 

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-docker/steps/3/1.JPG)

When the command executes, you see something like the following output:

```
Writing .gitignore
Writing host.json
Writing local.settings.json
Writing Dockerfile
```

After the project is created, use the following command to navigate to the new MyFunctionProj project folder.
`cd MyFunctionProj`{{execute}}


