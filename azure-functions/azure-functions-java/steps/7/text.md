Change directory to the newly created project folder (the one containing your host.json and pom.xml files) and build and run the function with Maven:

`cd fabrikam-functions`{{execute T1}}

`npm install -g azure-functions-core-tools`{{execute T1}}

`mvn clean package  && mvn azure-functions:run`{{execute T1}}
