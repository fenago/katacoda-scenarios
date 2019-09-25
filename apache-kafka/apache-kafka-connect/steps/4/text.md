Now, in the src/main/java/kioto/spark directory, open a file in **vscode** explorer called SparkProcessor.java with the contents of Listing 8.2, shown as follows:

```
package kioto.spark;
import kioto.Constants;
import org.apache.spark.sql.*;
import org.apache.spark.sql.streaming.*;
import org.apache.spark.sql.types.*;
import java.sql.Timestamp;
import java.time.LocalDate;
import java.time.Period;

public class SparkProcessor {
  private String brokers;
  public SparkProcessor(String brokers) {
    this.brokers = brokers;
  }
  public final void process() {
    //below is the content of this method
  }
  public static void main(String[] args) {
    (new SparkProcessor("localhost:9092")).process();
  }
}
```

Note that, as in previous examples, the main method invoked the process() method with the IP address and the port of the Kafka brokers.

Now, let's fill the process() method. The first step is to initialize Spark, as demonstrated in the following block:

```
SparkSession spark = SparkSession.builder()
    .appName("kioto")
    .master("local[*]")
    .getOrCreate();
```

In Spark, the application name must be the same for each member in the cluster, so here we call it Kioto (original, isn't it?).

As we are going to run the application locally, we are setting the Spark master to local[*], which means that we are creating a number of threads equivalent to the machine CPU cores.