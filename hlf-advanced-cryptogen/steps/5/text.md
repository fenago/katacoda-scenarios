In this step, we will extend the organization by adding a new peer.  Do this by creating a new yaml file and name it `extend-crypto-config.yaml` with only the new peer information that you are adding.  

<pre class="file" data-target="clipboard">
# Extends the crypto material for the setup
# Adds a new peer for Org1

#### Peers for acme
PeerOrgs:
  # Peer configuration for ACME
  - Name: Org1
    Domain: acme.com
    Specs:
      - Hostname: devpeer2
        CommonName: devpeer2

</pre>  

You can reate the crypto for the new peer with:
`cryptogen extend --help`{{copy}}
