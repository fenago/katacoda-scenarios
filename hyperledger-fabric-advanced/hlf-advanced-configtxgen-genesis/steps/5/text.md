
We also have to specify defaults for the orderer defined in the previous step.


```
# Configuration for the Orderer
Orderer: &OrdererDefaults

  OrdererType: solo

  Addresses:
    - localhost:7050

  # Batch Timeout: The amount of time to wait before creating a batch
  BatchTimeout: 2s

  # Batch Size: Controls the number of messages batched into a block
  BatchSize:
    MaxMessageCount: 10
    AbsoluteMaxBytes: 98 MB
    PreferredMaxBytes: 512 KB
```
