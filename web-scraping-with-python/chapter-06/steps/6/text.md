

Now that we have obtained all the filter `<form>-based` parameters for each authorTags, the final step is to submit these parameters—that is, params to filterurl—using HTTP POST and extract the resulting information:

```
#Step 3: load filterurl with author and defined tag
params = {'author': author, 'tag': tagSuccess, 'submit_button': submitButton, '__VIEWSTATE': viewstate}
customheaders = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': filterurl
}

finalResponse = processRequests(filterurl,params, customheaders)

#Step 4: Extract results
quote = finalResponse.find('div.quote span.content').text()

quoteAuthor = finalResponse.find('div.quote span.author').text()
message = finalResponse.find('div.quote span.tag').text()
print("Author: ", quoteAuthor, "\nMessage: ", message)
```

Form processing with searching and filtering actions, alongside the use of hidden fields, is shown in the preceding code. The ViewState value is used by the system behind the scenes to identify the selected option and filter the tags associated with it, resulting in quotes by the author.

The total number of HTTP POST parameters for the final form submission is four, whereas the page only displays or allows you to interact with two options. If any changes are made to a value, such as viewstate, or if viewstate is missing from params, it will result in empty quotes:

Form submission is not only dependent on the required parameters that are selected from visible `<form>` elements in the page—there can also be hidden values and dynamically generated state representation that should be processed and handled effectively for successful output. 

#### Run Code
Now, run the python code by running: `python toScrapeViewstate.py`{{execute}}


As we can see, finalResponse is a PyQuery object that's returned by processRequests() and is parsed to obtain the quote, quoteAuthor, and message, as shown in the following screenshot:


The output from iteration number one using the preceding code with Author and Message is as follows:

```
Author: Albert Einstein 
Message: success
```


The output from iteration number two using the preceding code with Author and Message is as follows:

```
Author: Thomas A. Edison 
Message: inspirational
```

In the next section, we will be dealing with form submission and user authentication.


