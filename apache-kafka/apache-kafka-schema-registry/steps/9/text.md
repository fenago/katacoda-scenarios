Deleting version 1 of the schema registered under the healthchecks-value subject
To delete version 1 of the schema registered under the healthchecks-value subject, you can use the following command:

`curl -X DELETE http://localhost:8081/subjects/healthchecks-value/versions/1`{{execute}}

The output should be something like this:

```
1
```

Deleting the most recently registered schema under the healthchecks-value subject

To delete the most recently registered schema under the healthchecks-value subject, you can use the following command:

`curl -X DELETE http://localhost:8081/subjects/healthchecks-value/versions/latest`{{execute}}

The output should be something like this:

```
2
```

Deleting all the schema versions registered under the healthchecks–value subject
To delete all the schema versions registered under the healthchecks-value subject, you can use the following command:

`curl -X DELETE http://localhost:8081/subjects/healthchecks-value`{{execute}}

The output should be something like this:
```
[3]
```
