Now try sending defective messages; first, try messages that are not in JSON format:

`I am not JSON, I am Freedy.`{{execute T1}} 

`I am a Kafkeeter!`{{execute T1}} 
 
This message should be received in the `invalid-messages` topic (and displayed in the window), as in the following example:

```
{"error": "JsonParseException: Unrecognized token ' I am not JSON, I am Freedy.': was expecting 'null','true', 'false' or NaN
at [Source: I am not JSON, I am Freedy.; line: 1, column: 4]"}
```

Then, let's try something more complex, the first message but without a timestamp, as in the example:

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "14862768", "name": "Snowden, Edward", "ipAddress": "95.31.18.111"}, "currency": {"name": "ethereum", "price": "RUB"}}`{{execute T1}} 

This message should be received in the `invalid-messages` topic, as follows:

```
{"error": "timestamp is missing."}
```

The message validation is complete.