We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_13/03_fid_cifar10.py` to view file.

#### Run Code

Now, run the python code by running: `python 03_fid_cifar10.py`{{execute}}

Running the example may take some time depending on the speed of your workstation. It
may also require a large amount of RAM. If you have trouble with the example, try halving the
number of samples to 5,000. At the end of the run, we can see that the FID score between the
train and test datasets is about five. Top-performing models at the time of writing are capable
of achieving a FID score of about 15 or 161.