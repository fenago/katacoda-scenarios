API is a service that's provided by web servers that are based on software architecture or principles. Simple Object Access Protocol (SOAP) and Representational State Transfer (REST) are methods for accessing web services. While REST is an architecture, SOAP is a protocol based on web standards. We will be dealing with the REST API in upcoming sections.

#### REST 
REST (https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) is a style of software architecture based on a set of defining and addressing network principles. REST is a software architecture, not a set of standards. REST uses standard HTTP protocol and methods such as GET, POST, PUT, and DELETE to provide services. It is stateless, multilayered, and also supports caching. 

Web APIs are generally classed as RESTful web services; they provide an interface to the user and other resources for communication. RESTful web services (REST APIs or web APIs) (https://restfulapi.net/) is the service provided by the web for adapting to the REST architecture. 

Services that are provided via REST don't need to be adapted to the new standards, development, or frameworks. Most of the time, it will be using a GET request, along with query strings that have been issued to APIs, searching for their response. HTTP status codes (https://restfulapi.net/http-status-codes/) (404, 200, 304) are often tracked to determine the response of an API. Responses can also be obtained in various formats, such as JSON, XML, and CSV.

In terms of choosing between REST and SOAP, REST is more easy and efficient when it comes to processing compared to SOAP, and is being provided to the public by a large number of websites. 

#### SOAP 
SOAP (https://www.w3.org/TR/soap/is) is a set of standards specified by W3C and also represents alternative to REST when it comes to web services. SOAP uses HTTP and SMTP (Simple Mail Transfer Protocol), and is used to exchange documents over the internet, as well as via remote procedures.

SOAP uses XML as a messaging service and is also known as an XML-based protocol. SOAP requests contain XML documents (with an envelope and body) that describes the methods and parameters that are sent to a server. The server will execute the method that's received, along with parameters, and send an SOAP response back to the program initiating the request.

SOAP is highly extensible and includes built-in error handling. It also works with other protocols, such as SMTP. SOAP is also independent to platforms and programming languages, and is mostly implemented in distributed enterprise environments.
