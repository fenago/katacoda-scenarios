Extracting the currency price
At the moment, Monedero has a service that validates the messages that are well formed. The service also enriches the messages with the customer's geographic location.

Recall that the Monedero core business is the cryptocurrencies exchange. So now, the business asks us for a service that returns the requested currency price online at a specific time.

To achieve this, we will use the exchange rate of open exchange rates: https://openexchangerates.org/

To obtain a free API key, you have to register in a free plan; the key is needed to access the free API [].

**Note:** api key is already provided in the source code as shown below. If you want to use your own key, you need to perform following steps.

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-enrichment/steps/7/0.JPG)


**Signup**

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-enrichment/steps/7/1.JPG)
	
**AppID**

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-enrichment/steps/7/2.JPG)


