We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_13/01_fid_numpy.py` to view file.

#### Run Code

Now, run the python code by running: `python 01_fid_numpy.py`{{execute}}

Running the example first reports the FID between the act1 activations and itself, which is
0.0 as we expect (note that the sign of the score can be ignored). The distance between the two
collections of random activations is also as we expect: a large number, which in this case was
about 359.

```
FID (same): -0.000
FID (different): 358.927
```

You may want to experiment with the calculation of the FID score and test other pathological
cases.