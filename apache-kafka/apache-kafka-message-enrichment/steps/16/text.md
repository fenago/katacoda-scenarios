From the first command-line terminal (the console producer), send the following three messages (remember to type enter between messages and execute each one in just one line):


{"event": "CUSTOMER_CONSULTS_ETHPRICE", "currency": {"name": "ethereum", "price": "USD"}, "timestamp": "2018-09-28T09:09:09Z"}

{"event": "CUSTOMER_CONSULTS_ETHPRICE", "currency": {"name": "ethereum", "price": "USD"}, "timestamp": "2018-09-28T08:08:14Z"}

{"event": "CUSTOMER_CONSULTS_ETHPRICE", "currency": {"name": "ethereum", "price": "USD"}, "timestamp": "2018-09-28T19:51:35Z"}


# Output
As these are valid messages, the messages typed in the producer console should appear in the valid-messages consumer console window, as in the example:

```
{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "14862768", "name": "Snowden, Edward", "ipAddress": "95.31.18.111", "country":"Russian Federation","city":"Moscow"}, "currency": {"name": "ethereum", "price": "USD", "rate":0.0049}, "timestamp": "2018-09-28T09:09:09Z"}

{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "13548310", "name": "Assange, Julian", "ipAddress": "185.86.151.11", "country":"United Kingdom","city":"London"}, "currency": {"name": "ethereum", "price": "USD", "rate":0.049}, "timestamp": "2018-09-28T08:08:14Z"}

{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "15887564", "name": "Mills, Lindsay", "ipAddress": "186.46.129.15", "country":"Ecuador","city":"Quito"}, "currency": {"name": "ethereum", "price": "USD", "rate":0.049}, "timestamp": "2018-09-28T19:51:35Z"}
```

 

