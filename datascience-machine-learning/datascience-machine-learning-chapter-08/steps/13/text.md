We're going to show the importance of cleaning your data. I have some web log data from a little website that I own. We are just going to try to find the top viewed pages on that website. Sounds pretty simple, but as you'll see, it's actually quite challenging! So, if you want to follow along, the `TopPages.ipynb` is the notebook that we're working from here. Let's start!


#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `TopPages.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/TopPages.ipynb

I actually have an access log that I took from my actual website. It's a real HTTP access log from Apache and is included in your book materials. So, if you do want to play along here, make sure you update the path to move the access log to wherever you saved the book materials:

```
logPath = "E:\\sundog-consult\\Packt\\DataScience\\access_log.txt"
```
