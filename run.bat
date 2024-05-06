rem Check if Python is installed
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
) else (
    rem Install Python
    echo Python is not installed. Installing...
    rem Download and install Python from the official website
    powershell -Command "& { Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python_installer.exe' }"
    python_installer.exe
    del python_installer.exe
)

rem Install required Python packages
echo Installing required Python packages...
python -m pip install pyside numpy matplotlib argparse math os tqdm

rem Run Python script
python ui.py
