Before we move on and explore pyquery and its features, let's start by installing it by using pip:

`pip install pyquery requests`{{execute}}

The following libraries are installed on a successful installation of pyquery using pip:

```
cssselect-1.0.3
lxml-4.3.1
pyquery-1.4.0
requests
 ```

`python`{{execute}}

`>>>` in the code represents the use of the Python IDE; it accepts the code or instructions and displays the output on the next line.
Once the installation is completed and successful, we can use pyquery, as shown in the following code, to confirm the setup. We can explore the properties it contains by using the dir() function:

`from pyquery import PyQuery as pq`{{execute}}

`print(dir(pq))`{{execute}}