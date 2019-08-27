
The process command generates default values from all dynamic expressions, making the template definition ready to be used for creating resources, which is done either by piping its output to the create command or by running the new-app command—we will get to that in a few moments. For now, let's use that command to see a List of objects to be created:


`oc process openshift//mariadb-persistent`{{execute}}
{
    "kind": "List",
    "apiVersion": "v1",
    "metadata": {},
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Secret",
            ...
            <output omitted>
            ...
            "stringData": {
                "database-name": "sampledb",
                "database-password": "tYuwInpmocV1Q1uy",
                "database-root-password": "icq5jd8bfFPWXbaK",
                "database-user": "userC7A"
            }
        },
        ...
        <output omitted>
        ...
    ]
}

Note: The process command allows for an alternate syntax, <NAMESPACE>//<TEMPLATE>. We used it here for demonstration purposes, but you are free to use the more familiar -n <NAMESPACE> notation.

The list is quite long, so we only provided an excerpt showing the Secret resource that contains all generated sensitive values that are to be used for template instantiation.

To make things clearer, let's take a look at the expressions for generating those values in the raw template definition:


`oc export template mariadb-persistent -n openshift`{{execute}}

apiVersion: v1
kind: Template
...
<output omitted>
...
objects:
- apiVersion: v1
  kind: Secret
  ...
  <output omitted>
  ... 
  stringData:
    database-name: ${MYSQL_DATABASE}
    database-password: ${MYSQL_PASSWORD}
    database-root-password: ${MYSQL_ROOT_PASSWORD}
    database-user: ${MYSQL_USER}
...
<output omitted>
...
parameters:
...
<output omitted>
...
- description: Username for MariaDB user that will be used for accessing the database.
  displayName: MariaDB Connection Username
from: user[A-Z0-9]{3}
  generate: expression
  name: MYSQL_USER
  required: true
...
<output omitted>
...
- description: Name of the MariaDB database accessed.
  displayName: MariaDB Database Name
  name: MYSQL_DATABASE
  required: true
value: sampledb
...
<output omitted>
...
You may have noticed, for example, that MYSQL_DATABASE is sampledb, while MYSQL_USER starts with the string user with three alphanumeric characters, just as we saw in the previous listing.

Note
To learn more about how to construct regular expressions for dynamic parameters, refer to http://perldoc.perl.org/perlre.html.