
By default, OpenShift comes installed with quite a few default templates, called Instant App and Quick Start templates. They can be used to deploy runtime environments based on various languages and frameworks, such as Ruby on Rails (Ruby), Django (Python), and CakePHP (PHP). They also include templates for SQL and NoSQL database engines with persistent storage, which includes PersistentVolumeClaims as one of the objects to provide persistence of data.


Default templates are created in the openshift project during installation. You can see them by running the following command:


`oc get template -n openshift | cut -d' ' -f1`{{execute}}

```
NAME
3scale-gateway
amp-apicast-wildcard-router
amp-pvc
cakephp-mysql-example
cakephp-mysql-persistent
dancer-mysql-example
dancer-mysql-persistent
django-psql-example
django-psql-persistent
dotnet-example
dotnet-pgsql-persistent
dotnet-runtime-example
httpd-example
```

We used the cut command to exclude descriptions and other information for the sake of brevity, but you can run this command without cut to see the full output.


To get a list of parameters that are supported by a particular template, use the process command:
`oc process --parameters mariadb-persistent -n openshift`{{execute}}

````
NAME                   DESCRIPTION       GENERATOR       VALUE
MEMORY_LIMIT           ...                               512Mi
NAMESPACE              ...                               openshift
DATABASE_SERVICE_NAME  ...                               mariadb
MYSQL_USER             ...               expression      user[A-Z0-9]{3}
MYSQL_PASSWORD         ...               expression      [a-zA-Z0-9]{16}
MYSQL_ROOT_PASSWORD    ...               expression      [a-zA-Z0-9]{16}
MYSQL_DATABASE         ...                               sampledb
MARIADB_VERSION        ...                               10.2
VOLUME_CAPACITY        ...                               1Gi
```

**Note:** We left out descriptions of the parameters to make the output more readable.

As you may have noticed, some parameters have dynamic default values, generated by expressions loosely based on Perl Compatible Regular Expressions (PCREs).