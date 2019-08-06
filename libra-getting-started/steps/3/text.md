Since the client is connected to a node on the testnet, you will see the following output.

```
usage: <command> <args>

Use the following commands:
...

Please, input commands:

libra%
```

**Note:** You can verify CLI Client Is Running on Your System by running `help`{{execute}} command. you should get 
**"connected to the validator"** as output.


You can also connect to a existing validator node running on the Libra testnet manually using following script.

```
./scripts/cli/start_cli_testnet.sh
```

This command builds and runs the client utilizing cargo (Rust’s package manager) and connects the client to a validator node on the testnet.

