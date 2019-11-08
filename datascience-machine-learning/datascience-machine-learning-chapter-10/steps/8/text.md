Now, it's a lot easier to talk about p-values than t-statistics because you don't have to think about, how many standard deviations are we talking about? What does the actual value mean? The p-value is a little bit easier for people to understand, which makes it a better tool for you to communicate the results of an experiment to the stakeholders in your business.

The p-value is basically the probability that this experiment satisfies the null hypothesis, that is, the probability that there is no real difference between the control and the treatment's behavior. A low p-value means there's a low probability of it having no effect, kind of a double negative going on there, so it's a little bit counter intuitive, but at the end of the day you just have to understand that a low p-value means that there's a high probability that your change had a real effect.

What you want to see are a high t-statistic and a low p-value, and that will imply a significant result. Now, before you start your experiment, you need to decide what your threshold for success is going to be, and that means deciding the threshold with the people in charge of the business.

So, what p-value are you willing to accept as a measure of success? Is it 1 percent? Is it 5 percent? And again, this is basically the likelihood that there is no real effect, that it's just a result of random variance. It is just a judgment call at the end of the day. A lot of times people use 1 percent, sometimes they use 5 percent if they're feeling a little bit riskier, but there's always going to be that chance that your result was just spurious, random data that came in.

However, you can choose the probability that you're willing to accept as being likely enough that this is a real effect, that's worth rolling out into production.

When your experiment is over, and we'll talk about when you declare an experiment to be over later, you want to measure your p-value. If it's less than the threshold you decided upon, then you can reject the null hypothesis and you can say "well, there's a high likelihood that this change produced a real positive or negative result."

If it is a positive result then you can roll that change out to the entire site and it is no longer an experiment, it is part of your website that will hopefully make you more and more money as time goes on, and if it's a negative result, you want to get rid of it before it costs you any more money.

**Note:**

Remember, there is a real cost to running an A/B test when your experiment has a negative result. So, you don't want to run it for too long because there's a chance you could be losing money.

This is why you want to monitor the results of an experiment on a daily basis, so if there are early indications that the change is making a horrible impact to the website, maybe there's a bug in it or something that's horrible, you can pull the plug on it prematurely if necessary, and limit the damage.

Let's go to an actual example and see how you might measure t-statistics and p-values using Python.

