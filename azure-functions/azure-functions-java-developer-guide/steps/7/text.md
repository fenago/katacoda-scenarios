
You can use Plain old Java objects (POJOs), types defined in azure-functions-java-library, or primitive data types such as String and Integer to bind to input or output bindings.

#### POJOs
For converting input data to POJO, azure-functions-java-worker uses the gson library. POJO types used as inputs to functions should be public.

#### Binary data
Bind binary inputs or outputs to byte[], by setting the dataType field in your function.json to binary:

```
   @FunctionName("BlobTrigger")
    @StorageAccount("AzureWebJobsStorage")
     public void blobTrigger(
        @BlobTrigger(name = "content", path = "myblob/{fileName}", dataType = "binary") byte[] content,
        @BindingName("fileName") String fileName,
        final ExecutionContext context
    ) {
        context.getLogger().info("Java Blob trigger function processed a blob.\n Name: " + fileName + "\n Size: " + content.length + " Bytes");
    }
```

If you expect null values, use **Optional<T>**.