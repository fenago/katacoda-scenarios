In the fourth command-line terminal, start up the processing engine. From the project root directory (where the gradle jar command were executed), run the following command:

`cd ~/kafka/Chapter02/monedero && java -jar ./build/libs/monedero-0.1.0.jar localhost:9092 foo input-topic valid-messages invalid-messages`{{execute T4}} 

**Important:** Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 4`.


#### Send Messages
From the **first** command-line terminal (the console producer), send the following three messages (remember to type enter between messages and execute each one in just one line):


`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "14862768", "name": "Snowden, Edward", "ipAddress": "95.31.18.111"}, "currency": {"name": "ethereum", "price": "RUB"}, "timestamp": "2018-09-28T09:09:09Z"}`{{execute T1}} 

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "13548310", "name": "Assange, Julian", "ipAddress": "185.86.151.11"}, "currency": {"name": "ethereum", "price": "EUR"}, "timestamp": "2018-09-28T08:08:14Z"}`{{execute T1}} 

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "15887564", "name": "Mills, Lindsay", "ipAddress": "186.46.129.15"}, "currency": {"name": "ethereum", "price": "USD"}, "timestamp": "2018-09-28T19:51:35Z"}`{{execute T1}} 

As these are valid messages, the messages typed in the producer console should appear in the valid-messages consumer console window.