# copy the script into the container; note: the resulting file is owned by root and it not executable
docker cp prepareContainer.sh jupyter:/tmp/prepareContainerRoot.sh
docker cp iris.csv jupyter:/tmp/iris.csv
docker cp pima-indians-diabetes.csv jupyter:/tmp/pima-indians-diabetes.csv
docker cp abalone.csv jupyter:/tmp/abalone.csv
#docker cp *.xlsx jupyter:/tmp/
# copy the script to make it accessible and executable 
docker exec -it jupyter bash -c 'cp /tmp/prepareContainerRoot.sh ~/prepareContainer.sh && chmod +x ~/prepareContainer.sh'
docker exec -it jupyter bash -c 'cp /tmp/iris.csv ~/iris.csv'
docker exec -it jupyter bash -c 'cp /tmp/pima-indians-diabetes.csv ~/pima-indians-diabetes.csv'
docker exec -it jupyter bash -c 'cp /tmp/abalone.csv ~/abalone.csv'
#docker exec -it jupyter bash -c 'cp /tmp/*.xlsx ~/'
# execute the script inside the container - to install a number of packages
docker exec -it jupyter bash -c './prepareContainer.sh'
# # restart the docker container
docker restart jupyter
echo 'restarted Jupyter container'
# perhaps clone a GitHub repo inside the Jupyter container
#docker exec -it jupyter git clone https://github.com/lucasjellema/DataAnalytics--IntroductionDataWrangling-JupyterNotebooks
# and more stuff?
docker logs jupyter
