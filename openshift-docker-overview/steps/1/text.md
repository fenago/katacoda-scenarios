Docker is the most popular container platform. It allows for creating, sharing, and running applications inside Docker containers. Docker separates running applications from the infrastructure. It allows you to speed up the application delivery process drastically. Docker also brings application development to an absolutely new level. I

#### Docker architecture

Docker uses a client-server type of architecture:

**Docker server:** This is a service running as a daemon in an operating system. This service is responsible for downloading, building, and running containers.
**Docker client:** The CLI tool is responsible for communicating with Docker servers using the REST API.

To complete this step, run a small custom container.

This container just displays the time every second.
`docker run jpetazzo/clock`{{execute}}

- This container will run forever.
- To stop it, press ^C.
- Docker has automatically downloaded the image jpetazzo/clock.
- This image is a user image, created by jpetazzo.