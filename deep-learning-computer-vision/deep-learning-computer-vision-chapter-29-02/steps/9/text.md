We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_29/07_face_verification.py` to view file.

#### Run Code

We can test out some positive examples by downloading more photos of Sharon Stone from
Wikipedia. 

- sharon_stone2.jpg
- sharon_stone3.jpg

We will test these two positive cases and the Channing Tatum photo from the previous
section as a negative example. The complete code example of face verification is listed below

Now, run the python code by running: `python 07_face_verification.py`{{execute}}

The first photo is taken as the template for Sharon Stone and the remaining photos in the
list are positive and negative photos to test for verification. Running the example, we can see
that the system correctly verified the two positive cases given photos of Sharon Stone both
earlier and later in time. We can also see that the photo of Channing Tatum is correctly not
verified as Sharon Stone. It would be an interesting extension to explore the verification of other
negative photos, such as photos of other female celebrities.

```
Positive Tests
>face is a Match (0.418 <= 0.500)
>face is a Match (0.295 <= 0.500)
Negative Tests
>face is NOT a Match (0.709 > 0.500)
```
