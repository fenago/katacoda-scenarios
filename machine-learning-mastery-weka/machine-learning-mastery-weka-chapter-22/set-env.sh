
docker run -d --network host --privileged --name kali-desktop athertahir/kali-weka

docker exec -it kali-desktop bash -c "mkdir -p /root/Desktop/weka && cp -r /usr/share/doc/weka/ /root/Desktop && cd /root/Desktop && wget https://netix.dl.sourceforge.net/project/weka/datasets/datasets-numeric/datasets-numeric.jar && unzip datasets-numeric.jar && cp /root/Desktop/numeric/housing.arff /root/Desktop/numeric/housing-numeric.arff && sed -i 's/@attribute CHAS { 0, 1}/@attribute CHAS real/g' /root/Desktop/numeric/housing-numeric.arff"
