You can also choose to run your functions directly from the deployment package file. This method skips the deployment step of copying files from the package to the wwwroot directory of your function app. Instead, the package file is mounted by the Functions runtime, and the contents of the wwwroot directory become read-only.

Zip deployment integrates with this feature, which you can enable by setting the function app setting `WEBSITE_RUN_FROM_PACKAGE` to a value of `1`. 


**Benefits of running from a package file**

There are several benefits to running from a package file:

- Reduces the risk of file copy locking issues.
- Can be deployed to a production app (with restart).
- You can be certain of the files that are running in your app.
- Improves the performance of Azure Resource Manager deployments.
- May reduce cold-start times, particularly for JavaScript functions with large npm package trees.