The application requires a single HTTP API endpoint that takes an image URL as the input and returns a prediction of whether the image contains a dog or a cat.

In the terminal, use the Azure Functions Core Tools to scaffold a new HTTP function named classify.
`func new --language python --template HttpTrigger --name classify`{{execute T1}}

A new folder named classify is created, containing two files.

- **__init__.py:** A file for the main function
- **function.json:** A file describing the function's trigger and its input and output bindings

**Note:** You can have a look at the files in **vscode** editor by clicking `IDE editor` tab and navigating to `functions-python-tensorflow-tutorial` > `start` folder. Refresh explorer if you don't see classify folder.