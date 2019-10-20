In the following example, we will use the select() function to list the `<li>` element with the data-id attribute:

`soup = BeautifulSoup(html_doc,'lxml')`{{execute}}

`print(soup.select('li[data-id]'))`{{execute}}

As seen in the preceding code, the `li[data-id]` selector queries the `<li>` element with the attribute key named as data-id. The Value for data-id is empty, which allows traversing through all `<li>` possessing data-id. The result is obtained as a list of objects, in which indexes can be applied to fetch the exact elements as seen in the following code:

`print(soup.select('ul li[data-id]')[1]) #fetch index 1 only from resulted List`{{execute}}

`print(soup.select_one('li[data-id]'))`{{execute}}


