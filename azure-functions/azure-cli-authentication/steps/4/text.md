
Service principals are accounts not tied to any particular user, which can have permissions on them assigned through pre-defined roles. Authenticating with a service principal is the best way to write secure scripts or programs, allowing you to apply both permissions restrictions and locally stored static credential information. 

To sign in with a service principal, you need:

- The URL or name associated with the service principal
- The service principal password, or the X509 certificate used to create the service principal in PEM format
- The tenant associated with the service principal, as either an .onmicrosoft.com domain or Azure object ID