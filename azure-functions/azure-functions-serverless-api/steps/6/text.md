
Repeat the steps to Create a function app to create a new function app in which you will create your proxy. This new app's URL will serve as the frontend for our API, and the function app you were previously editing will serve as a backend.

1. Navigate to your new frontend function app in the portal.

2. Select **Platform Features** and choose Application Settings.

3. Scroll down to **Application settings** where key/value pairs are stored and create a new setting with key "HELLO_HOST". Set its value to the host of your backend function app, such as `<YourBackendApp>.azurewebsites.net`. This is part of the URL that you copied earlier when testing your HTTP function. You'll reference this setting in the configuration later.

    **Note:** App settings are recommended for the host configuration to prevent a hard-coded environment dependency for the proxy. Using app settings means that you can move the proxy configuration between environments, and the environment-specific app settings will be applied.

4. Click **Save**.
