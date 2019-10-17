In this section, we will develop a face detection system to predict the identity of a given face.
The model will be trained and tested using the 5 Celebrity Faces Dataset that contains many
photographs of five different celebrities. We will use an MTCNN model for face detection, the
FaceNet model will be used to create a face embedding for each detected face, then we will
develop a Linear Support Vector Machine (SVM) classifier model to predict the identity of a
given face.


#### Celebrity Faces Dataset
The 5 Celebrity Faces Dataset is a small dataset that contains photographs of celebrities. It
includes photos of: Ben Affleck, Elton John, Jerry Seinfeld, Madonna, and Mindy Kaling. The
dataset was prepared and made available by Dan Becker and provided for free download on
Kaggle. Note, a Kaggle account is required to download the dataset.

Folder name 5-celebrity-faces-dataset has been already created for you. You should
now have a directory with the following structure (note, there are spelling mistakes in some
directory names, and they were left as-is in this example):


We can see that there is a training dataset and a validation or test dataset. Looking at
some of the photos in the directories, we can see that the photos provide faces with a range of
orientations, lighting, and in various sizes. Importantly, each photo contains one face of the
person. We will use this dataset as the basis for our classifier, trained on the train dataset only
and classify faces in the val dataset. You can use this same structure to develop a classifier
with your own photographs