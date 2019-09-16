You can create a script, say helloworld.ps1, and save it to your clouddrive to use it across shell sessions.

<pre class="file" data-target="clipboard">

cd $HOME\clouddrive

# Create a new file in clouddrive directory
New-Item helloworld.ps1

# Open the new file for editing
code .\helloworld.ps1

# Add the content, such as 'Hello World!'
.\helloworld.ps1
Hello World!

</pre>

Next time when you use PowerShell in Cloud Shell, the `helloworld.ps1` file will exist under the `$HOME\clouddrive` directory that mounts your Azure Files share.