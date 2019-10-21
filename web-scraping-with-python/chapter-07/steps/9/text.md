In this example, we will be collecting information regarding type (type of event), created_at (date of event created), id (event identification code), and repo (repository name) across pages. We will be using the following URL: https://api.github.com/events.

GitHub Events lists public activities that have been performed within the past 90 days. These events are provided in pages, with 30 items per page, and a maximum of 300 being shown. Various sections exist inside events, all of which reveal the description about the actor, repo, org, created_at, type, and more. 

For more details, please refer to the following link: https://developer.github.com/v3/activity/events/.

Here is the code we will be using:

```
if __name__ == "__main__":
    eventTypes=[] 
    #IssueCommentEvent,WatchEvent,PullRequestReviewCommentEvent,CreateEvent
    
    for page in range(1, 4): #First 3 pages
        events = readUrl('events?page=' + str(page))
        
        for event in events:
            id = event['id']
            type = event['type']
            actor = event['actor']['display_login']
            repoUrl = event['repo']['url']
            createdAt = event['created_at']
            eventTypes.append(type)
            dataSet.append([id, type, createdAt, repoUrl, actor])

    eventInfo = dict(Counter(eventTypes))
    
    print("Individual Event Counts:", eventInfo)
    print("CreateEvent Counts:", eventInfo['CreateEvent'])
    print("DeleteEvent Counts:", eventInfo['DeleteEvent'])

print("Total Events Found: ", len(dataSet))
print(dataSet)
```

The preceding code gives us the following output:

```
Status Code: 200
Headers: Content-Type: application/json; charset=utf-8
................
Status Code: 200
Headers: Content-Type: application/json; charset=utf-8

Individual Event Counts: {'IssueCommentEvent': 8, 'PushEvent': 42, 'CreateEvent': 12, 'WatchEvent': 9, 'PullRequestEvent': 10, 'IssuesEvent': 2, 'DeleteEvent': 2, 'PublicEvent': 2, 'MemberEvent': 2, 'PullRequestReviewCommentEvent': 1}

CreateEvent Counts: 12
DeleteEvent Counts: 2
Total Events Found: 90

[['9206862975','PushEvent','2019-03-08T14:53:46Z','https://api.github.com/repos/CornerYoung/MDN','CornerYoung'],'https://api.github.com/repos/OUP/INTEGRATION-ANSIBLE','peter-masters'],.....................,'2019-03-08T14:53:47Z','https://api.github.com/repos/learn-co-curriculum/hs-zhw-shoes-layout','maxwellbenton']]
```

The Counter class from the collections Python module is used to obtain the individual count of elements from eventTypes: 

```
from collections import Counter
```

#### Run Code
Now, run the python code by running: `python githubevent.py`{{execute}}