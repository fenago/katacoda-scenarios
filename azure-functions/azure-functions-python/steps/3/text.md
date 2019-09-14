To locally develop and test Python functions, it is recommended to use a Python 3.6 environment. Run the following commands to create and activate a virtual environment named .venv.

Azure Functions requires Python 3.6.x. You'll create a virtual environment to ensure you're using the required Python version.

`apt-get update`{{execute T1}}

`yes | apt-get install python3-venv`{{execute T1}}

`python3.6 -m venv .venv`{{execute T1}}

`source .venv/bin/activate`{{execute T1}}
