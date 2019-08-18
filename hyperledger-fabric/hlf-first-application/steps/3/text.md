The following instructions require you to be in the fabcar/javascript subdirectory within your local clone of the fabric-samples repo `cd javascript`{{execute T1}}

Run the following command to install the Fabric dependencies for the applications. It will take few moments to complete: `npm install`{{execute T1}}

This process is installing the key application dependencies defined in package.json. The most important of which is the fabric-network class; it enables an application to use identities, wallets, and gateways to connect to channels, submit transactions, and wait for notifications. 

Once npm install completes, everything is in place to run the application. For this tutorial, you’ll primarily be using the application JavaScript files in the `fabcar/javascript` directory. Let’s take a look at what’s inside: `ls`{{execute T1}}

You should see the following:

```
enrollAdmin.js  node_modules  package.json
registerUser.js invoke.js     package-lock.json 
query.js        wallet
```