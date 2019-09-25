
Now that we're in the src/main/java/kioto/plain directory, let's have  look at the `PlainProcessor.java` file:

The following is the content of `PlainProcessor.java` (part 2):

```
 public final void process() {
    consumer.subscribe(Collections.singletonList(
               Constants.getHealthChecksTopic()));           //1
    while(true) {
      ConsumerRecords records = consumer.poll(Duration.ofSeconds(1L)); //2
      for(Object record : records) {                //3
        ConsumerRecord it = (ConsumerRecord) record;
        String healthCheckJson = (String) it.value();
        HealthCheck healthCheck = null;
        try {
          healthCheck = Constants.getJsonMapper()
           .readValue(healthCheckJson, HealthCheck.class);     // 4
        } catch (IOException e) {
            // deal with the exception
        }
        LocalDate startDateLocal =healthCheck.getLastStartedAt().toInstant()                   .atZone(ZoneId.systemDefault()).toLocalDate();        //5
        int uptime =
             Period.between(startDateLocal, LocalDate.now()).getDays();  //6
        Future future =
             producer.send(new ProducerRecord<>(
                              Constants.getUptimesTopic(),
                              healthCheck.getSerialNumber(),
                              String.valueOf(uptime)));                  //7
        try {
          future.get();
        } catch (InterruptedException | ExecutionException e) {
          // deal with the exception
        }
      }
    }
  }
  public static void main( String[] args) {
    (new PlainProcessor("localhost:9092")).process();
  }
}
````

An analysis of the PlainProcessor includes the following:

- In line `//1`, the consumer is created and subscribed to the source topic. This is a dynamic assignment of the partitions to our customer and join to the customer group. 
- In line `//2`, an infinite loop to consume the records, the pool duration is passed as a parameter to the method pool. The customer waits no longer than one second before return.
- In line `//3`, we iterate over the records.
- In line `//4`, the JSON string is deserialized to extract the health check object.
- In line `//5`, the start time is transformed formatted at the current time zone.
- In line `//6`, the uptime is calculated.
- In line `//7`, the uptime is written to the uptimes topic, using the serial number as the key and the uptime as value. Both values are written as normal strings.

The moment at which the broker returns records to the client also depends on the fetch.min.bytes value; its default is 1, and is the minimum data amount to wait before the broker is available to the client. Our broker returns as soon as 1 byte of data is available, while waiting a maximum of one second.

The other configuration property is fetch.max.bytes, which defines the amount of data returned at once. With our configuration, the broker will return all of the available records (without exceeding the maximum of 50 MB).

If there are no records available, the broker returns an empty list.

**Note** that we could reuse the producer that generates the mock data, but it is clearer to use another producer to write uptimes.

