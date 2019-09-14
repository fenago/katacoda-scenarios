Import the TensorFlow model
You'll use a pre-built TensorFlow model that was trained with and exported from Azure Custom Vision Service.

 Note

If you want to build your own using Custom Vision Service's free tier, you can follow the instructions in the sample project repository.

The model consists of two files in the <REPOSITORY_ROOT>/resources/model folder: model.db and labels.txt. Copy them into the classify function's folder.

Linux and macOS:
bash

Copy
cp ../resources/model/* classify


Be sure to include the * in the above command. Confirm that classify now contains files named model.pb and labels.txt.