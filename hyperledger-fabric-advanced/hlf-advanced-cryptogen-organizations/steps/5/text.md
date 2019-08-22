In this step, we will add more organization to the cryptogen yaml file.

<pre class="file" data-filename="config.yaml">

  # ---------------------------------------------------------------------------
  # Org2: See "Org1" for full specification
  # ---------------------------------------------------------------------------
  - Name: Org2
    Domain: org2.example.com
    EnableNodeOUs: false
    Template:
      Count: 1
    Users:
      Count: 1
	  
</pre>


You can generate the crypto material by running: `cryptogen generate --config ~/config.yaml --output ~/crypto-config`{{execute}}

#### Output
You will get both organization's domain name as a output.
```
org1.example.com
org2.example.com
```

#### OrdererOrganizations
You can verify that orderer organization has been created by running following command. Orderer needs access to MSP & TLS.
`cd ~/crypto-config/ordererOrganizations/example.com/ && ls`{{execute}}

Orderer will only contain default Admin user because we didn't create any other users `cd users && ls`{{execute}}

#### PeerOrganizations
You can verify that peers orgs have been created by running following command. Orderer needs access to MSP & TLS.
`cd ~/crypto-config/peerOrganizations/ && ls`{{execute}}

Peer will also contain another user `User1@org1.example.com` other than default Admin user bacause we specified user count equal to tone in config.yaml  `cd org1.example.com/users/ && ls`{{execute}}