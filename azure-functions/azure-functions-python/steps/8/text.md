You'll use a pre-built TensorFlow model that was trained with and exported from Azure Custom Vision Service.


The model consists of two files in the <REPOSITORY_ROOT>/resources/model folder: `model.db` and `labels.txt`. ` them into the classify function's folder.

`cp ../resources/model/* classify`{{execute T1}}

Be sure to include the * in the above command. Confirm that classify now contains files named model.pb and labels.txt.