The second step is to code the HealthCheck class. This class is a Plain Old Java Object (POJO). The model class is the template for the value object.

Open the project with your favorite IDE and, in the src/main/java/kioto directory, open a file in **vscode** explorer called HealthCheck.java with the content of Listing 4.4.


```
package kioto;
import java.util.Date;
public final class HealthCheck {
  private String event;
  private String factory;
  private String serialNumber;
  private String type;
  private String status;
  private Date lastStartedAt;
  private float temperature;
  private String ipAddress;
}
```

With your IDE, generate the following:

A no-parameter constructor
A constructor with all of the attributes passed as parameters
The getters and the setters for each attribute
This is a data class, a POJO in Java. In languages such as Kotlin, the model classes require so much less boilerplate code, but now we are in Java. Some purists of object-oriented programming argue that value objects is an object-oriented anti-pattern. However, the serialization libraries to produce messages need these classes.

To generate fake data with JavaFaker, our code should be as shown in Listing 4.5.

The following is the content of Listing 4.5, a health check mock generator with JavaFaker:

```
HealthCheck fakeHealthCheck =
   new HealthCheck(
        "HEALTH_CHECK",
        faker.address().city(),                    //1
        faker.bothify("??##-??##", true),    //2
              Constants.machineType.values()
                   [faker.number().numberBetween(0,4)].toString(), //3
        Constants.machineStatus.values()
                   [faker.number().numberBetween(0,3)].toString(), //4
        faker.date().past(100, TimeUnit.DAYS),           //5
        faker.number().numberBetween(100L, 0L),          //6
        faker.internet().ipV4Address());                 //7
```

The following is an analysis of how to generate fake health check data:

- In line `//1`, address().city() generates a fictitious city name
- In line `//2`, in the expression ? for alpha # for numeric, true if alpha is uppercase
- In line `//3`, we use the machine type enum in Constants , and a fake number between 0 and 4
- In line `//4`, we use the machine status enum in Constants and a fake number between 0 and 3, inclusively
- In line `//5`, we are saying that we want a fake date between the past 100 days from today
- In line `//6`, we build a fake IP address

Here, we depend on the attributes order of the constructor. Other languages, such as Kotlin, allow specifying each assigned attribute name.

Now, to transform our Java POJO into a JSON string, we use the method in the Constants class—something like the following:

```
String fakeHealthCheckJson fakeHealthCheckJson = Constants.getJsonMapper().writeValueAsString(fakeHealthCheck);
```

Don't forget that this method throws a JSON processing exception.