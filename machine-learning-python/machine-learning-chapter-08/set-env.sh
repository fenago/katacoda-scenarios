docker run -p 8888:8888 -d --name jupyter fenago/lv-ml-jupyter:v1

# copy the script into the container; note: the resulting file is owned by root and it not executable
docker cp prepareContainer.sh jupyter:/tmp/prepareContainerRoot.sh

docker cp  ~/tutorial/. jupyter:/home/jovyan/work

# copy file from fenago jupyter image to work folder.
docker exec -it jupyter bash -c 'if [ -f "/home/jovyan/winequality-white.csv" ]; then rm -rf /home/jovyan/work/winequality-white.csv && cp /home/jovyan/winequality-white.csv /home/jovyan/work/winequality-white.csv; fi'

# copy the script to make it accessible and executable 
docker exec -it jupyter bash -c 'cp /tmp/prepareContainerRoot.sh ~/prepareContainer.sh && chmod +x ~/prepareContainer.sh'
# execute the script inside the container - to install a number of packages
docker exec -it jupyter bash -c './prepareContainer.sh'
# # restart the docker container
docker restart jupyter
echo 'restarted Jupyter container'

docker logs jupyter