One way for auditing selection bias issues is running what's called an A/A test, like we saw earlier. So, if you actually run an experiment where there is no difference between the treatment and control, you shouldn't see a difference in the end result. There should not be any sort of change in behavior when you're comparing those two things.

An A/A test can be a good way of testing your A/B framework itself and making sure there's no inherent bias or other problems, for example, session leakage and whatnot, that you need to address.

Data pollution
Another big problem is data pollution. We talked at length about the importance of cleaning your input data, and it's especially important in the context of an A/B test. What would happen if you have a robot, a malicious crawler that's crawling through your website all the time, doing an unnatural amount of transactions? What if that robot ends up getting either assigned to the treatment or the control?

That one robot could skew the results of your experiment. It's very important to study the input going into your experiment and look for outliers, then analyze what those outliers are, and whether they should they be excluded. Are you actually letting some robots leak into your measurements and are they skewing the results of your experiment? This is a very, very common problem, and something you need to be cognizant of.

There are malicious robots out there, there are people trying to hack into your website, there are benign scrapers just trying to crawl your website for search engines or whatnot. There are all sorts of weird behaviors going on with a website, and you need to filter out those and get at the people who are really your customers and not these automated scripts. That can actually be a very challenging problem. Yet another reason to use off-the-shelf frameworks like Google Analytics, if you can.
