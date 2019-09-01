In the previous sections, we saw that containers can be created and deleted easily. But when a container is deleted, all the data associated with that container disappears too. That is why a lot of people refer to containers as a stateless architecture. But we can change this behavior and keep all the data by using persistent volumes. In order to enable persistent storage for a Docker container, we need to use the -v option, which binds the container filesystem to the host filesystem that runs that container.

In the next example, we will create a MariaDB container with persistent storage in the /mnt/data folder on the host. Then, we delete the MariaDB container and recreate it again using the same persistent storage.

First, remove all previously created containers:
`docker rm -f $(docker ps -aq)`{{execute}}

We have to prepare persistent storage on the node before we begin. Be aware that we need to give read/write permissions to the persistent storage directory. The MariaDB application works with a MySQL user with UID=999 inside the container. Also, it is important to mention that the special SE Linux security context svirt_sandbox_file_t is required. This can be achieved using the following commands:

`mkdir /mnt/data && chown 999:999 /mnt/data`{{execute}}

`chcon -Rt svirt_sandbox_file_t /mnt/data`{{execute}}

The next step is to create the container running the MariaDB service:
`docker run -d -v /mnt/data:/var/lib/mysql --name mariadb -e MYSQL_ROOT_PASSWORD=password mariadb`{{execute}}


Run the docker ps command: `docker ps`{{execute}}

```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
41139532924e mariadb "docker-entrypoint.sh" 4 seconds ago Up 3 seconds 3306/tcp mariadb
```

Create a new database and verify the existence of this new DB:
`docker exec -it mariadb mysql -uroot -ppassword -e "create database persistent;"`{{execute}}

`docker exec -it mariadb mysql -uroot -ppassword -e "show databases;"`{{execute}}

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| persistent         |
+--------------------+
```

Verify that there is new data in the /mnt/data directory created by the mariadb container. This is how we make the data persistent:


`ls -l /mnt/data/`{{execute}}
drwx------. 2 polkitd ssh_keys 4096 Mar 6 16:18 mysql
drwx------. 2 polkitd ssh_keys 20 Mar 6 16:18 performance_schema
drwx------. 2 polkitd ssh_keys 20 Mar 6 16:23 persistent
...
output truncated for brevity
...


Delete the mariadb container and verify that all files will be kept:
`docker rm -f mariadb`{{execute}}

`ls -l /mnt/data/`{{execute}}

```
drwx------. 2 polkitd ssh_keys 4096 Mar 6 16:18 mysql
drwx------. 2 polkitd ssh_keys 20 Mar 6 16:18 performance_schema
drwx------. 2 polkitd ssh_keys 20 Mar 6 16:23 persistent
...
output truncated for brevity
...
```