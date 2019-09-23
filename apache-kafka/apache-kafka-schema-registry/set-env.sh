wget -qO - https://packages.confluent.io/deb/3.3/archive.key | apt-key add -

add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/3.3 stable main"

apt-get update

yes | apt-get install confluent-platform-oss-2.11


curl -L https://cnfl.io/cli | sh -s -- -b /usr/local/bin

confluent local start --path /usr

clear