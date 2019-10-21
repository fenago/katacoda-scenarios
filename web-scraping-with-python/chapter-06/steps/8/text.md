Let's continue with form submission, but with invalid credentials. The paramsIncorrect phrase contains an invalid value for password:

```
 paramsIncorrect = {username: 'admin', password: '123456'} #Access Denied
 print(paramsIncorrect)
 processParams(paramsIncorrect)
```

The preceding code will result in the following output:

```
{'pwd': '123456', 'usr': 'admin'}
Confirm Login : ACCESS DENIED!
```

The preceding output can also be found in the loginUrl itself, and no redirection takes place this time:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-06/steps/8/1.png)

`Access Denied! (processed with wrong credentials)`

As you can see, user authentication and form submission work in tandem. With the use of proper login credentials and by being able to handle the form submission process using Python, we can obtain a successful output or deal with the related output that's returned from a website. 

In the next section, we will be performing form submission and user authentication by handling cookies that contain a session.

#### Run Code
Now, run the python code by running: `python testingGroundCookie.py`{{execute}}

