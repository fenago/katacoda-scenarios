Example Dataset Structure
We can make the image dataset structure concrete with an example. Imagine we are classifying
photographs of cars, as we discussed in the previous section. Specifically, a binary classification
problem with red cars and blue cars. We must create the directory structure outlined in the
previous section, specifically:

```
data/
data/train/
data/train/red/
data/train/blue/
data/test/
data/test/red/
data/test/blue/
data/validation/
data/validation/red/
data/validation/blue/
```

We must have different photos for each of the train, test, and validation datasets. In the
interest of keeping this tutorial focused, we will re-use the same image files in each of the three
datasets but pretend they are different photographs. Place copies of the red car 01.jpg file in
data/train/red/, data/test/red/, and data/validation/red/ directories. Now place copies
of the blue car 01.jpg file in data/train/blue/, data/test/blue/, and data/validation/blue/
directories. We now have a very basic dataset layout that looks like the following (output from
the tree command):

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-08/steps/4/1.JPG)

**Note:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_08/data` folder to view files.