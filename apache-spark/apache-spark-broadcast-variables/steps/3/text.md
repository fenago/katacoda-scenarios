

- Broadcast variables are the shared variables, which allow Spark to send large values efficiently in an immutable (read-only) state to all the worker nodes.
- These variables can be used one or more times during Spark operations. 
- The broadcast variables are sent to the worker nodes only once and are then cached to the worker nodes’ memory in deserialized form. 
- These variables are very useful when the Spark job consists of multiple stages and multiple tasks in those stages require the same variable. 
- Broadcast Variables overcome the inefficiency of shipping the variables every time to executors.

Using Broadcast Variables doesn’t mean that the data is not transmitted across the network. But unlike transmitting the data everytime the variable is referenced in the `regular` variables, the data is only transmitted once saving network bandwidth and executor resources.

#### Optimizing Broadcast Variables
It is important to optimize Broadcast Variables with compact and fast data serialization when large values are used to broadcast. Not doing so will result in network bottlenecks, if the value takes too muct time to serialize and transmit over the network. Using the correct serialization library will help improve the job performance in an efficient manner.
