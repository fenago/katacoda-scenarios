
- Open a Terminal and change directory to where you downloaded your key pair.

- If you have not already done so, restrict the access permissions on your key pair file.
This is required as part of the SSH access to your server. For example, open a terminal on
your workstation and type:
```
cd Downloads
chmod 600 keras-aws-keypair.pem
```

- Click Launch Instances. If this is your first time using AWS, Amazon may have to
validate your request and this could take up to 2 hours (often just a few minutes).

- Click View Instances to review the status of your instance.

Your server is now running and ready for you to log in.