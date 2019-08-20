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


You can generate the crypto material by running: `cryptogen generate --config ./config.yaml`{{copy}}

#### Output
You will get both organization's name created as a output.

```
```

`cd ~/first-network`{{execute}}

`cd ~/first-network`{{execute}}


Validate that the crypto material was created for the organizations by going into the generated crypto-config DIRECTORY and then navigate to peerOrganizations. Explore the various directories

You can reate the crypto for the new peer with:
`cryptogen extend --help`{{copy}}
