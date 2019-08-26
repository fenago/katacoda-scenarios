Let's try to start a database container again by providing all required variables:

`docker run -d --name mariadb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=example -e MYSQL_USER=example_user -e MYSQL_PASSWORD=password mariadb`{{execute}}
721dc752ed0929dbac4d8666741b15e1f371aefa664e497477b417fcafee06ce
Run the docker ps command to verify that the container is up and running:


`docker ps`{{execute}}
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
721dc752ed09 mariadb "docker-entrypoint.sh" 10 seconds ago Up 9 seconds 3306/tcp mariadb
The container was created successfully. Run the verification command to check that example_user has access to the example database:


`docker exec -it mariadb mysql -uexample_user -ppassword example -e "show databases;"`{{execute}}
+--------------------+
| Database           |
+--------------------+
| example            |
| information_schema |
+--------------------+
The startup script created a user named example_user with the password password as we specified in the environment variables. It also configured a password for the root user. The full list of MariaDB image variables you can specify is located at https://hub.docker.com/_/mariadb/.
