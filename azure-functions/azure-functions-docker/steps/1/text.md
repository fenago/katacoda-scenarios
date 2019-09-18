Azure Functions lets you host your functions on Linux in your own custom container. You can also host on a default Azure App Service container. This functionality requires the Functions `2.x` runtime.

In this scenario, you learn how to deploy your functions to Azure as a custom Docker image. This pattern is useful when you need to customize the built-in container image. You may want to use a custom image when your functions need a specific language version or require a specific dependency or configuration that isn't provided within the built-in image.

This scenario walks you through how to use Azure Functions Core Tools to create a function in a custom Linux image. You publish this image to a function app in Azure, which was created using the Azure CLI.

In this scenario, you learn how to:

- Create a function app and Dockerfile using Core Tools.
- Build a custom image using Docker.
- Publish a custom image to a container registry.
- Create an Azure Storage account.
- Create a Premium hosting plan.
- Deploy a function app from Docker Hub.
- Add application settings to the function app.