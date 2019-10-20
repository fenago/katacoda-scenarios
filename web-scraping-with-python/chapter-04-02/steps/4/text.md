The page URL that's passed to get_details() is read by read_url() and response from a PyQuery object is obtained. Information that contains blocks are identified as articles using CSS selectors. Since there's more than one articles iteration available, we use items(). Individual data elements are then processed with the help of cleaning, replacing, and merging activities before they are appended to the main dataset, which in this case is dataSet. PyQuery expressions can also be shortened via the use of articlebody.

Also, the remove() PyQuery (manipulation) method is used to remove .ibm--card__date, which is found inside `<h5>`, in order to obtain atype. The atype content would also contain additional .ibm--card__date details if used without removing with the following code:

```
articlebody.find('h5 > .ibm--card__date').remove())
```


#### Run Code
Now, run the python code by running: `python example1_ibm_announcements.py`{{execute}}

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/example1_ibm_announcements.py` to view python code file.
