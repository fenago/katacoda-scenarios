Open the build.gradle file on the Monedero project created in Chapter 2, Message Validation, and add the lines highlighted in Listing 3.1.

The following is the content of Listing 3.1, the Monedero build.gradle file:

Copy
apply plugin: 'java'
apply plugin: 'application'
sourceCompatibility = '1.8'
mainClassName = 'monedero.ProcessingEngine'
repositories {
  mavenCentral()
}
version = '0.2.0'
dependencies {
    compile group: 'org.apache.kafka', name: 'kafka_2.12', version:                                                                                                                                              
                                                            '2.0.0'
compile group: 'com.maxmind.geoip', name: 'geoip-api', version:                                         
                                                            '1.3.1'
    compile group: 'com.fasterxml.jackson.core', name: 'jackson-core', version: '2.9.7'
}
jar {
  manifest {
    attributes 'Main-Class': mainClassName
  } from {
    configurations.compile.collect {
      it.isDirectory() ? it : zipTree(it)
    }
  }
  exclude "META-INF/*.SF"
  exclude "META-INF/*.DSA"
  exclude "META-INF/*.RSA"
}
Listing 3.1: build.gradle

Note that the first change is the switch from version 0.1.0 to version 0.2.0 .

The second change is to add the MaxMind's GeoIP version 1.3.1 to our project.

From the project root directory, run the following command to rebuild the app:

Copy
$ gradle jar
The output is something like the following:

Copy
...BUILD SUCCESSFUL in 8s