The easiest way to install binding extensions is to enable extension bundles. When you enable bundles, a predefined set of extension packages is automatically installed.

To enable extension bundles, open the `host.json` file in **vscode** editor by clicking `IDE editor` tab and navigating to `MyFunctionProj` folder and update its contents to match the following code:

<pre class="file" data-target="clipboard">
{
    "version": "2.0",
    "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[1.*, 2.0.0)"
    }
}
</pre>
