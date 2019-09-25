Now, in the src/main/java/kioto/custom directory, open a file in **vscode** explorer called CustomProducer.java with the content of Listing 4.13.

The following is the content of Listing 4.13, CustomProducer.java:

```
package kioto.plain;
import ...
public final class CustomProducer {
  /* here the Constructor code in Listing 4.12 */
  public void produce(int ratePerSecond) {
    long waitTimeBetweenIterationsMs = 1000L / (long)ratePerSecond; //1
    Faker faker = new Faker();
    while(true) { //2
      HealthCheck fakeHealthCheck /* here the code in Listing 4.5 */;
      Future futureResult = producer.send( new ProducerRecord<>(
         Constants.getHealthChecksTopic(), fakeHealthCheck));       //3
      try {
        Thread.sleep(waitTimeBetweenIterationsMs); //4
        futureResult.get();      //5          
      } catch (InterruptedException | ExecutionException e) {
        // deal with the exception
      }
    }
  }
public static void main(String[] args) {
    new CustomProducer("localhost:9092").produce(2); //6
  }
}
```


An analysis of the `CustomProducer` class includes the following:

- In line `//1`, ratePerSecond is the number of messages to send in a one-second period
- In line `//2`, to simulate repetition, we use a infinite loop (try to avoid this in production)
- In line `//3`, we use a Java future to send the message to HealthChecksTopic
- In line `//4`, we wait this time to send messages again
- In line `//5`, we read the result of the future created previously
- In line `//6`, everything runs on the broker in localhost in port 9092, sending two messages in an interval of one second
 

