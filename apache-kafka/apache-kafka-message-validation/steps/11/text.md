In the third command-line terminal, start the processing engine. Go to the project root directory where the gradle jar command was executed and run, as follows:

`cd ~/kafka/Chapter02/monedero && java -jar ./build/libs/monedero-0.1.0.jar localhost:9092 foo input-topic output-topic`{{execute T3}}

Now, the show consists in reading all of the events from input-topic and writing them in output-topic.

**Important:** Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 3`.


#### First terminal
Go to the `first` command-line terminal (the message producer) and send the following three messages :

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "14862768", "name": "Snowden, Edward", "ipAddress": "95.31.18.111"}, "currency": {"name": "ethereum", "price": "RUB"}, "timestamp": "2018-09-28T09:09:09Z"}`{{execute T1}} 

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "13548310", "name": "Assange, Julian", "ipAddress": "185.86.151.11"}, "currency": {"name": "ethereum", "price": "EUR"}, "timestamp": "2018-09-28T08:08:14Z"}`{{execute T1}} 

`{"event": "CUSTOMER_CONSULTS_ETHPRICE", "customer": {"id": "15887564", "name": "Mills, Lindsay", "ipAddress": "186.46.129.15"}, "currency": {"name": "ethereum", "price": "USD"}, "timestamp": "2018-09-28T19:51:35Z"}`{{execute T1}} 

If everything is working fine, the messages typed in the console-producer should be appearing in the console-consumer window, because the processing engine is copying from `input-topic` to `output-topic`. Switch back to `terminal 2` to confirm.

**Note:** Press `Ctrl` + `C` in terminal 1, 2 & 3 to stop everything before proceeding to next step.