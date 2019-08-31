Adding templates
Once a template is developed, it can be added to OpenShift like any other YAML or JSON-defined objects, using the oc create command. It is a common practice to use a separate tenant specifically for templates, which will be shared between multiple projects. A default installation of the Red Hat OpenShift Container Platform (OCP) provides a number of templates in the openshift project. All of an OpenShift cluster's users have read access to the project, but only the cluster admin is able to modify or create templates in the project.

The following example shows how to add a template to your current project:
`oc create -f mytemplate.yaml`{{execute}}

`oc get template`{{execute}}

```
NAME        DESCRIPTION    PARAMETERS    OBJECTS
template1                  1 (1 blank)   1
```

OpenShift template overview
An OpenShift template is a set of API resources that can be parameterized and processed to produce a list of objects for creation by OpenShift. A template can be processed to create any desired OpenShift objects (such as deployment configurations, build configurations, and so on). A template can also define a set of labels to apply to every object defined in the template. You can apply a template by using the CLI or the web console. For example, a template might contain two pods (an application and a database), a service, and a route. Once the template has been developed, you can reuse it.

 

 

Template syntax
Templates, like any other OpenShift resources, can be created from a raw YAML or JSON definition. An example is as follows:


`cat mytemplate.yaml
apiVersion: v1
kind: Template 
metadata:
  name: template1
objects: 
- apiVersion: v1
  kind: Pod
  metadata:
    name: app1
  spec:
    containers:
    - env:
      - name: SHOW_DATA
        value: ${SHOW_DATA} 
      image: example/appimage
      name: app1
      ports:
      - containerPort: 8080
        protocol: TCP
parameters: 
- description: Myapp configuration data
  name: SHOW_DATA
  required: true
labels: 
  mylabel: app1
The preceding example includes only one resource—a pod named app1. It also includes a parameter—SHOW_DATA. Parameters can be used to customize application deployment and accommodate all kinds of use cases.

 

 

Parameters can also have the following default values: 


parameters: 
- description: Myapp configuration data
  name: SHOW_DATA
  required: true
  value: Example value
In some cases, we may want to generate values according to a certain pattern, as shown here:


parameters:
  - description: Password used for Redis authentication
    from: '[A-Z0-9]{8}'
    generate: expression
    name: REDIS_PASSWORD
In the preceding example, instantiating the template will generate a random password, eight characters long, consisting of all upper and lowercase alphabet letters, as well as numbers. Although that syntax is highly reminiscent of regular expressions, it implements only a small subset of Perl Compatible Regular Expressions (PCRE), so you can still use the \w, \d, and \a modifiers:

[w]{10}: This expands to 10 alphabet characters, numbers, and underscores. This follows the PCRE standard and is the same as [a-zA-Z0-9_]{10}.
[\d]{10}: This expands to 10 numbers. This is the same as [0-9]{10}.
 [\a]{10}: This expands to 10 alphabetical characters. This is the same as [a-zA-Z]{10}.
This capability is very useful for generating random passwords.

Note
It's important to understand that the process of parameter expansion takes place when resources are being created from the template, not when the template itself is created; so, each generated resource gets its own unique value.

Adding templates
Once a template is developed, it can be added to OpenShift like any other YAML or JSON-defined objects, using the oc create command. It is a common practice to use a separate tenant specifically for templates, which will be shared between multiple projects. A default installation of the Red Hat OpenShift Container Platform (OCP) provides a number of templates in the openshift project. All of an OpenShift cluster's users have read access to the project, but only the cluster admin is able to modify or create templates in the project.

The following example shows how to add a template to your current project:


`oc create -f mytemplate.yaml
template "template1" created

`oc get template
NAME        DESCRIPTION    PARAMETERS    OBJECTS
template1                  1 (1 blank)   1
You will need to become the system:admin user to create a template in the openshift tenant:


`oc login -u system:admin

`oc create -f mytemplate.json -n openshift
template "template1" created

`oc get template -n openshift|grep temp
template1