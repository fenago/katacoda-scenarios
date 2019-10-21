The following code shows use of some functions such as sub() (that is, re.sub()), strip(), and replace() are used in many places and can also be used for the purpose of cleaning:


`dealerInfo = re.split(r'<br>', re.sub(r'<br><br>', '', '<br>a<br>b'))`

`stock = list(map(lambda stock:stock.strip(),availability))`

`availability = stockPath(row)[0].strip()`

`article['lastUpdated'] = article['lastUpdated'].replace('This page was last edited on', '')`

`title = row.find(attrs={'itemprop':'text'}).text.strip()`

`re.sub(r'or\s*','',fortran)`

`dealerInfo = re.split(r'<br>',re.sub(r'<br><br>','',dealer))`
