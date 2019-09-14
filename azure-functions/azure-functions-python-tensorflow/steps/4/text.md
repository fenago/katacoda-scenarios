Azure Functions requires Python 3.6.x. You'll create a virtual environment to ensure you're using the required Python version.

Change the current working directory to the start folder. Then create and activate a virtual environment named `.venv`.

`apt-get update`{{execute T1}}

`yes | apt-get install python3-venv`{{execute T1}}

`cd start && python3.6 -m venv .venv`{{execute T1}}

`source .venv/bin/activate`{{execute T1}}

The terminal prompt is now prefixed with `(.venv)` which indicates you have successfully activated the virtual environment. Confirm that python in the virtual environment is indeed Python `3.6.x`.

`python --version`{{execute T1}}