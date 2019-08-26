The next step is to run a WordPress container. In that command, we will link the wordpress container with the mariadb container:
`docker run -d --name wordpress --link mariadb:mysql -p 8080:80 wordpress`{{execute}}

Unable to find image 'wordpress:latest' locally
Trying to pull repository docker.io/library/wordpress ...
latest: Pulling from docker.io/library/wordpress
...
output truncated for brevity
...
Digest: sha256:670e4156377063df1a02f036354c52722de0348d46222ba30ef6a925c24cd46a
1f69aec1cb88d273de499ca7ab1f52131a87103d865e4d64a7cf5ab7b430983a
Let's check container environments with the docker exec command:


`docker exec -it wordpress env|grep -i mysql
MYSQL_PORT=tcp://172.17.0.2:3306
MYSQL_PORT_3306_TCP=tcp://172.17.0.2:3306
MYSQL_PORT_3306_TCP_ADDR=172.17.0.2
MYSQL_PORT_3306_TCP_PORT=3306
MYSQL_PORT_3306_TCP_PROTO=tcp
...
output truncated for brevity
...