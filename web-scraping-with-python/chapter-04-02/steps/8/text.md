Let's do some more processing. Each `<tr>` or tr element is an item of tableRows and is traversed with the help of the items() method to find the exact `<td>` or td by using their index and retrieving the data it contains:

```
for tr in tableRows.items():
    #few <tr> contains single <td> and is omitted using the condition
    team1 = tr.find('td').eq(1).text() 

    if team1 != '':
        game_date = tr.find('td').eq(0).text()
        dates = re.search(r'(.*)-(.*)-(.*)',game_date)
        team1_score = tr.find('td').eq(2).text()
        team2 = tr.find('td').eq(4).text()
        team2_score = tr.find('td').eq(5).text()

        #check Game Status should be either 'W' or 'L'
        game_status = tr.find('td').eq(6).text()
        if not re.match(r'[WL]',game_status):
            game_status = tr.find('td').eq(7).text()

        #breaking down date in year,month and day
        year = dates.group(3)
        month = dates.group(2)
        day = dates.group(1)

        #preparing exact year value
        if len(year)==2 and int(year)>=68:
            year = '19'+year
        elif len(year)==2 and int(year) <68:
            year = '20'+year
        else:
            pass
```

So far, the desired data from the targeted `<td>` has been collected and also formatted in the case of year. Regex has also been applied in the code and used with dates and game_status. Finally, the collected objects are appended as a list to dataSet:

```
#appending individual data list to the dataSet
dataSet.append([year,month,day,game_date,team1,team1_score,team2,team2_score,game_status])

print("\nTotal Game Status, found :", len(dataSet))
print(dataSet)
```

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/example3_AHL.py` to view python code file.

#### Run Code
Now, run the python code by running: `python example3_AHL.py`{{execute}}
