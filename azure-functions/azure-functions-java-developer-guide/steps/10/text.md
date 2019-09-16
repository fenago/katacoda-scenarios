These are defined in azure-functions-java-library. They are helper types to work with HttpTrigger functions.

Specialized type |	Target | Typical usage
--- | --- | ---
`HttpRequestMessage<T>` | `HTTP Trigger` | Gets method, headers, or queries
`HttpResponseMessage` | `HTTP Output Binding` | Returns status other than 200