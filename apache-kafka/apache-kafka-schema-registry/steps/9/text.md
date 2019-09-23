Deleting version 1 of the schema registered under the healthchecks-value subject
To delete version 1 of the schema registered under the healthchecks-value subject, you can use the following command:

`curl -X DELETEcurl -X DELETE http://localhost:8081/subjects/healthchecks-avro-value/versions/1`{{execute}}

The output should be something like this:

```
1
```

#### Protip
Deleting the most recently registered schema under the healthchecks-value subject

To delete the most recently registered schema under the healthchecks-value subject, you can use the following command:

`curl -X DELETE http://localhost:8081/subjects/healthchecks-avro-value/versions/latest`


Deleting all the schema versions registered under the healthchecks–value subject
To delete all the schema versions registered under the healthchecks-value subject, you can use the following command:

`curl -X DELETE http://localhost:8081/subjects/healthchecks-value`
