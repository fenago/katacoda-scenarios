Now, the Schema Registry is running on port 8081. To interact with the Schema Registry, there is a REST API. We can access it with curl. The first step is to register a schema in the Schema Registry. To do so, we have to embed our JSON schema in another JSON object, and we have to escape some special characters and add a payload:

- At the beginning, we have to add `{ \"schema\": \"`
- All the double quotation marks (") should be escaped with a backslash (`\"`)
- At the end, we have to add `\" }`

Yes, as you can guess, the API has several commands to query the Schema Registry.

 