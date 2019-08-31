Let's delete the user and its identity to provide a clean slate for the upcoming demonstrations:


`oc delete user/alice`{{execute}}

```
user "alice" deleted
```

`oc delete \
identity/LDAP:uid=alice,cn=users,cn=accounts,dc=idm,dc=example,dc=com`{{execute}}

