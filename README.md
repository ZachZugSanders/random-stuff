# Install Python 3.13

1. Go to the [Python 3.13 download page](https://www.python.org/downloads/release/python-3130/) and download the Windows installer.
2. Run the installer and follow the prompts to install Python.
3. Make sure to select the option to add Python to your PATH during the install process.
4. After the install is complete, open a new command prompt or PowerShell and type `python --version` to verify that Python 3.13 is installed correctly.

## Update PYTHONPATH

1. Right-click on "Computer" or "This PC" and select "Properties".
2. Click on "Advanced system settings" on the left side.
3. Click on "Environment Variables".
4. Under "System Variables", scroll down and find the "Path" variable, then click "Edit".
5. Click "New" and enter the path to the Python 3.13 executable (e.g. `C:\Python313\bin\python.exe`).
6. Click "OK" to close all the windows.

## Install uv package

1. Open a new command prompt or PowerShell.
2. Type `pip install uv` to install the uv package.
3. Once the install is complete, type `uv --version` to verify that the uv package is installed correctly.

## Create uv virtual environment

1. Open a new command prompt or PowerShell.
2. Type `uv venv` to create a virtual environment.
3. Once the virtual environment is created, type `uv venv --activate` to activate the virtual environment.
4. Type `uv --version` to verify that the virtual environment is activated.

## Install Selenium

1. Open a new command prompt or PowerShell.
2. Type `uv pip install selenium` to install the Selenium package.
3. Once the install is complete, type `selenium --version` to verify that the Selenium package is installed correctly.

## Run the script

1. Open a new command prompt or PowerShell.
2. Type `uv run main.py` to run the script.
3. Once the script is running, type `uv --version` to verify that the script is running correctly.
