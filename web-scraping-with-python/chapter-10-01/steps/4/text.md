We have needed to extract lines of data throughout this book. You may have noticed that, in most of these examples, we used a dataset (a Python list object that was used to collect data) that was appended with various fields in a Python list, as shown in the following code (collected from various examples of this book):

```
dataSet.append([year,month,day,game_date,team1,team1_score,team2,team2_score,game_status])
```

```
dataSet.append([title,price,availability,image.replace('../../../..',baseUrl),rating.replace('star-rating ','')])
```

```
dataSet.append([link, atype, adate, title, excerpt,",".join(categories)])
```

```
dataSet.append([titleLarge, title, price, stock, image, starRating.replace('star-rating ', ''), url])
```

With the availability of such a dataset, we can write this information to external files, as well as to the database. Before we write the dataset to the files, column names that describe the data from the dataset are needed. Consider the following code, where keys is a separate list containing a string title, that is, the name of the columns to the respective list item appended to the dataset:

```
keys = ['year','month','day','game_date','team1', 'team1_score', 'team2', 'team2_score', 'game_status']
......
dataSet.append([year,month,day,game_date,team1,team1_score,team2,team2_score,game_status])
```

