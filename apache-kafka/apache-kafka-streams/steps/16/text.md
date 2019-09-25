To test the Kafka Streams solution for late events, the first thing we need is a late event generator.

To simplify things, our generator will constantly send events at a fixed rate. And from time to time, it will generate a late event. The generator generates events with the following process:

- Each window is 10 seconds long
- It produces one event every second
- The event should be generated in 54th second of each minute, and will be delayed by 12 seconds; that is, it will arrive in the sixth second of the next minute (in the next window)

When we say that the window is of 10 seconds, we mean that we will make aggregations every 10 seconds. Remember that the objective of the test is that the late events are counted in the correct window.

Create the src/main/java/kioto/events directory and, inside it, open a file in **vscode** explorer called EventProducer.java with the contents of Listing 6.5, shown as follows:

```
package kioto.events;
import ...
public final class EventProducer {
  private final Producer<String, String> producer;
  private EventProducer(String brokers) {
    Properties props = new Properties();
    props.put("bootstrap.servers", brokers);
    props.put("key.serializer", StringSerializer.class);
    props.put("value.serializer", StringSerializer.class);
    producer = new KafkaProducer<>(props);
  }
  private void produce() {
    // ...
  }
  private void sendMessage(long id, long ts, String info) {
    // ...
  }
  public static void main(String[] args) {
    (new EventProducer("localhost:9092")).produce();
  }
}
```

The event generator is a Java KafkaProducer, so declare the same properties as all the Kafka Producers.

The generator code is very simple, and the first thing that is required is a timer that generates an event every second. The timer triggers 0.3 seconds after every second to avoid messages sent at 0.998 seconds, for example. The produce() method is shown as follows:

```
private void produce() {
  long now = System.currentTimeMillis();
  long delay = 1300 - Math.floorMod(now, 1000);
  Timer timer = new Timer();
  timer.schedule(new TimerTask() {
    public void run() {
      long ts = System.currentTimeMillis();
      long second = Math.floorMod(ts / 1000, 60);
      if (second != 54) {
        EventProducer.this.sendMessage(second, ts, "on time");
      }
      if (second == 6) {
        EventProducer.this.sendMessage(54, ts - 12000, "late");
      }
    }
  }, delay, 1000);
}
```

When the timer is triggered, the run method is executed. We send one event each second except on second 54, where we delay this event by 12 seconds. Then, we send this late event in the sixth second of the next minute, modifying the timestamp.

In the `sendMessage()` method, we just assign the timestamp of the event, shown as follows:

```
private void sendMessage(long id, long ts, String info) {
  long window = ts / 10000 * 10000;
  String value = "" + window + ',' + id + ',' + info;
  Future futureResult = this.producer.send(
     new ProducerRecord<>(
          "events", null, ts, String.valueOf(id), value));
  try {
    futureResult.get();
  } catch (InterruptedException | ExecutionException e) {
    // deal with the exception
  }
}
```
