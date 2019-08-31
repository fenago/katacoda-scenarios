
Once both the Jenkins and MongoDB pods are running, go back to the Builds | Pipelines sub-menu: 


Click the Start Pipeline button. This will trigger a CI/CD pipeline, to start building. Depending on your internet connection, this step will take some time to complete; by the end of it, you should be able to see that two stages were completed successfully:


Clicking on View Log should open a new tab with the Jenkins console output from the Jenkins login page:


Jenkins login page

Click on Log in with OpenShift and use the same credentials that you used to authenticate in OpenShift (use the developer user, with any password):


Jenkins user authorization

You will need to authorize the developer user to access Jenkins, by clicking on Allow selected permissions. This will get you to the Jenkins Console Output:


Jenkins Console Output

Scroll down to see the complete log, close the lab, and go back to the OpenShift tab.  

Note
If you are interested in how Jenkins works in detail and want to learn more, just follow the links in the Further reading section of this chapter. 

We mentioned previously that there is a difference between the Continuous Delivery and Continuous Deployment models; one of them includes human intervention, and the other one does not. 

What we are going to do next is modify our test pipeline and add an approval step. 