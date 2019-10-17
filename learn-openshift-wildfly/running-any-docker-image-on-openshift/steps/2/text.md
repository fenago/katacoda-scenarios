In this tutorial we will learn how to run a Docker image, built from a Dockerfile, on Openshift.

So our starting point will be a simple Dockerfile definition which pulls the default "WildFly" image and adds some customizations to it. In our case, it simply adds a management user:

<pre class="file" data-filename="Dockerfile" data-target="replace">
FROM jboss/wildfly
RUN /opt/jboss/wildfly/bin/add-user.sh admin Password1! --silent
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement","0.0.0.0"]
</pre>