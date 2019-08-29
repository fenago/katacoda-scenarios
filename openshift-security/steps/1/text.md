In this step, we will learn OpenShift CLI using the command _oc_. We can deploy new applications in OpenShift cluster.

Run the folowing command to login as admin in the OpenShift cluster
``oc login -u system:admin``{{execute HOST1}}

# Output

```
You have access to the following projects and can switch between them with 'oc project <projectname>':

  * default
    kube-public
    kube-system
    openshift
    openshift-infra
```

# Openshift Project
Openshift Project is similar to the Kubernetes namespace which also supports access controls for different users.

To complete this step, create a new project called ``myproject`` using CLI.


Users and identities
A user is any human actor that can make requests to the OpenShift API to access resources and perform actions. Users are typically created in an external identity provider, usually a corporate identity management solution such as Lightweight Directory Access Protocol (LDAP) or Active Directory.

To support multiple identity providers, OpenShift relies on the concept of identities serving as a bridge between users and identity providers. By default, a new user and identity are created upon the first login.


Go to https://172.24.0.11:8443 in your web browser and you will see the login page:


Log in via browser using the username alice and the password supersecret, and observe that the user was created using CLI:

oc get user

```
NAME    UID      FULL NAME     IDENTITIES
alice bf11471e-47a8-11e8-8dee-525400daa710  Alice Springs   LDAP:uid=alice,cn=users,cn=accounts,dc=idm,dc=example,dc=com
```

You can also see that an identity was created as well and mapped to the user:

oc get identity


Authentication
The term authentication refers to the process of validating one's identity. Usually, users aren't created in OpenShift itself, but provided by an external entity, such as the LDAP server or GitHub. The only part where OpenShift steps in is authorization—determining roles and, therefore, permissions for a user. OpenShift supports integration with various identity management solutions used in corporate environments, such as FreeIPA/Identity Management, Active Directory, GitHub, Gitlab, OpenStack Keystone, and OpenID. For the purpose of brevity, we will only discuss the most commonly used ones, but you can refer to https://docs.openshift.org/latest/install_config/configuring_authentication.html for the complete documentation.

Users and identities
A user is any human actor that can make requests to the OpenShift API to access resources and perform actions. Users are typically created in an external identity provider, usually a corporate identity management solution such as Lightweight Directory Access Protocol (LDAP) or Active Directory.

To support multiple identity providers, OpenShift relies on the concept of identities serving as a bridge between users and identity providers. By default, a new user and identity are created upon the first login. There are four ways to map users to identities:

Method

Description

claim

If a user with the same name already exists and is mapped to another identity, creation of another identity and login will fail. This is useful when you want to maintain a clear separation between identities provided by several providers in the case of identical usernames. A potential use case for this method would be transitioning from one authentication scheme to another.

add

If a user with the same name already exists and is mapped to another identity, another identity mapped to the same user is created. This is useful if you need to provide users from separate organizational entities that have their own identity management solutions with the ability to authenticate using mechanisms that are convenient for them.

lookup

OpenShift looks up an existing user, identity, and mapping, but doesn't create any of them, so these entities must exist prior to the user being able to log in.

generate

If a user with the same name already exists and is mapped to another identity, a separate user mapped to this identity is generated.

Go to https://172.24.0.11:8443 in your web browser and you will see the login page where you can choose from available identity providers:


Log in via browser with the LDAP identity provider using the username alice and the password supersecret, and observe that the user was created using CLI:

Copy
# oc get user
NAME    UID      FULL NAME     IDENTITIES
alice bf11471e-47a8-11e8-8dee-525400daa710  Alice Springs   LDAP:uid=alice,cn=users,cn=accounts,dc=idm,dc=example,dc=com
Note
Notice that identity's name is composed of its type and user locator, delimited by colon. Locator is provider-specific and specifies how to request a particular user from a specific provider.

You can also see that an identity was created as well and mapped to the user:

Copy
# oc get identity
NAME  IDP  NAME  IDP  USER NAME                                             USER   NAME  USER UID
LDAP:uid=alice,cn=users,cn=accounts,dc=idm,dc=example,dc=com   LDAP            uid=alice,cn=users,cn=accounts,dc=idm,dc=example,dc=com   alice       bf11471e-47a8-11e8-8dee-525400daa710
Let's try to log in with the PASSWORD_FILE provider using the same credentials:


The credentials are correct, but OpenShift was unable to create a new identity and identity mapping to an existing user, as the user was already claimed by the LDAP provider. This is exactly what the message Could not create user indicates.