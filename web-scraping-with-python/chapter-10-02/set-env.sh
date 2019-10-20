docker run -d --user root -p 8888:8888 --name jupyter -e GRANT_SUDO=yes jupyter/scipy-notebook:83ed2c63671f start-notebook.sh

# copy the script into the container; note: the resulting file is owned by root and it not executable
docker cp prepareContainer.sh jupyter:/tmp/prepareContainerRoot.sh

docker cp  ~/tutorial/. jupyter:/home/jovyan/work

# copy the script to make it accessible and executable 
docker exec -it jupyter bash -c 'sudo chmod -R 777 ~ && cp /tmp/prepareContainerRoot.sh ~/prepareContainer.sh && chmod +x ~/prepareContainer.sh && ~/prepareContainer.sh'

# # restart the docker container
docker restart jupyter
echo 'restarted Jupyter container'

docker logs jupyter