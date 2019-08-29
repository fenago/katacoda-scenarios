Displaying template parameters
The OpenShift community has developed many useful OpenShift templates, to deploy a number of well-known services. Once the template is determined, you will need to understand which parameters it accepts.

There are a couple of ways to list all of the parameters:

Using the oc process --parameters command (this is the easiest one)
Looking for the parameters section in the template's definition
Among many others, the OpenShift default installation comes with the mariadb-persistent template, as shown here:

Copy
# oc get template mariadb-persistent -n openshift
NAME  DESCRIPTION  PARAMETERS OBJECTS
mariadb-persistent MariaDB database service, with persistent storage. For more information about... 8 (3 generated) 4
That template has a number of parameters, listed as follows:

Copy
# oc process --parameters -n openshift mariadb-persistent
NAME DESCRIPTION GENERATOR VALUE
...
<output omitted>
...
VOLUME_CAPACITY Volume space available for data, e.g. 512Mi, 2Gi. 1Gi
If you don't want to import the template into OpenShift, the same method allows you to display the parameters of a locally stored OpenShift template:

Copy
# oc process --parameters -f mytemplate.yaml
NAME        DESCRIPTION  GENERATOR    VALUE
SHOW_DATA   Myapp configuration data
Another method is to use the oc describe command:

Copy
# oc describe template template1
Name:        template1
Namespace:    myproject
...
<output omitted>
...
Parameters:
    Name:        SHOW_DATA
    Description:    Myapp configuration data
    Required:        true
    Value:        <none>
...
<output omitted>
...