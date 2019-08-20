

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{copy}} the command to download and install cryptogen utility.

#### Validate
You can verify cryptogen is installed on your System by running `cryptogen version`{{copy}} command.

#### Usage
Here’s some examples using the different available flags on the peer command `cryptogen --help`{{copy}}

```
usage: cryptogen [<flags>] <command> [<args> ...]

Utility for generating Hyperledger Fabric key material

Flags:
  --help  Show context-sensitive help (also try --help-long and --help-man).

Commands:
  help [<command>...]
    Show help.

  generate [<flags>]
    Generate key material

  showtemplate
    Show the default configuration template

  version
    Show version information

  extend [<flags>]
    Extend existing network
```
