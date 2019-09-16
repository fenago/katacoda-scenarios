If you specify only the major version ("~2" for 2.x or "~1" for 1.x), the function app is automatically updated to new minor versions of the runtime when they become available. New minor versions do not introduce breaking changes. If you specify a minor version (for example, "2.0.12345"), the function app is pinned to that specific version until you explicitly change it.

**Note:**
If you pin to a specific version of Azure Functions, and then try to publish to Azure using Visual Studio, a dialog window will pop up prompting you to update to the latest version or cancel the publish. To avoid this, add the following property in your .csproj file.

`<DisableFunctionExtensionVersionUpdate>true</DisableFunctionExtensionVersionUpdate>`{{copy}}

When a new version is publicly available, a prompt in the portal gives you the chance to move up to that version. After moving to a new version, you can always use the FUNCTIONS_EXTENSION_VERSION application setting to move back to a previous version.

A change to the runtime version causes a function app to restart.

The values you can set in the `FUNCTIONS_EXTENSION_VERSION` app setting to enable automatic updates are currently **"~1"** for the `1.x` runtime and **"~2"** for `2.x`.