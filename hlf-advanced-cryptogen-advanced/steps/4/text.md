Following yaml contains OrdererOrgs which contains the definition of organizations managing orderer nodes

<pre class="file" data-filename="config.yaml" data-target="replace">

OrdererOrgs:
  # ---------------------------------------------------------------------------
  # Orderer
  # ---------------------------------------------------------------------------
  - Name: Orderer
    Domain: example.com
    Specs:
      - Hostname: orderer
	  
</pre>


Following yaml defines PeerOrgs which contains the definition of organizations managing peer nodes. Template allows for the definition of 1 or more hosts that are created sequentially.


<pre class="file" data-filename="config.yaml">

PeerOrgs:
  # ---------------------------------------------------------------------------
  # Org1
  # ---------------------------------------------------------------------------
  - Name: Org1
    Domain: org1.example.com
    EnableNodeOUs: false

    # ---------------------------------------------------------------------------
    # "Template"
    # ---------------------------------------------------------------------------
    # Allows for the definition of 1 or more hosts that are created sequentially
    # from a template. By default, this looks like "peer%d" from 0 to Count-1.
    # You may override the number of nodes (Count), the starting index (Start)
    # or the template used to construct the name (Hostname).
    Template:
      Count: 1
    # ---------------------------------------------------------------------------
    # "Users"
    # ---------------------------------------------------------------------------
    # Count: The number of user accounts _in addition_ to Admin
    # ---------------------------------------------------------------------------
    Users:
      Count: 1
	  
</pre>

#### Validate
Validate that the crypto material was created for the organizations by going into the generated crypto-config DIRECTORY and then navigate to peerOrganizations. Explore the various directories