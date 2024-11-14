# Background Service Project

This project contains Python scripts that perform various tasks such as printing the system time, checking network connectivity, making API calls with retries, simulating network blocking, and logging the results to a file. Below is the setup guide to test and run each script.

## Project Setup

Before testing the scripts, you need to set up the project environment. Please follow the instructions below to install the necessary dependencies and run the scripts.

### 1. Clone the Repository (if applicable)

If the project is hosted on a Git repository, you can clone it using:

```bash
git clone https://github.com/EjiroOsiephri/Python-Task-Solution.git
cd Python-Task-Solution
```

### 2. Create and Activate the Virtual Environment

Create a Virtual Environment: First, create a virtual environment in the project root directory:

```bash
python -m venv venv

```

Activate the Virtual Environment:

On Windows:

```bash

.\venv\Scripts\activate
```

On macOS/Linux:

```bash

source venv/bin/activate

```

Once activated, your terminal should reflect the virtual environment as the current active environment.

3. Install Dependencies
   With the virtual environment activated, install the project dependencies:

bash

pip install -r requirements.txt
Installed packages include:

requests: For making HTTP requests.
schedule: For scheduling tasks to run periodically. 4. Verify Installation
Ensure that everything is set up correctly by running:

```bash

pip freeze
```

This will list all installed dependencies, which should include requests and schedule.

Scripts Overview
This project includes four main Python scripts:

background_service.py: Runs a background service that prints the current time and checks network connectivity every 30 seconds.

api_call_with_retries.py: Makes an API call with retry logic, retrying up to three times if the request fails.

network_blocking.py: Simulates blocking network requests to specific domains.

file_logging_system.py: Logs successful API calls to a file with timestamps and response status.

Testing the Scripts

1. Test the Background Service (background_service.py)
   Steps to Run:

Open a terminal window.
Ensure the virtual environment is activated.
Navigate to the scripts folder if needed.
Run the script:

```bash

python background_service.py
```

Expected Output: Every 30 seconds, you will see:

Current time: The system’s current date and time.
Network status: Whether the network is connected or disconnected.

Example:

```bash
Current time: 2024-11-15 14:00:30.123456
Network is connected
```

To stop the script, press Ctrl + C.

2. Test API Call with Retries (api_call_with_retries.py)
   Steps to Run:

Open a terminal window and activate the virtual environment.
Navigate to the scripts folder.
Run the script:

python api_call_with_retries.py
Expected Output: If successful, the JSON response will be printed:

json

{
"userId": 1,
"id": 1,
"title": "delectus aut autem",
"completed": false
}
If the request fails, retry messages will appear:

```php

Attempt 1 failed: <error_message>
```

3. Test Network Blocking Simulation (network_blocking.py)
   Steps to Run:

Open a terminal window and activate the virtual environment.
Navigate to the scripts folder.
Run the script:

```bash

python network_blocking.py
Expected Output: Blocked domains will show:
```

Access to https://example.com is blocked.
Other requests will show responses or errors:

```php
Request failed: <error_message>
```

4. Test the File Logging System (file_logging_system.py)
   Steps to Run:

Open a terminal window and activate the virtual environment.
Navigate to the scripts folder.
Run the script:

```bash

python file_logging_system.py
```

Expected Output: Successful calls will log:

```mathematica

2024-11-15 14:00:30 - Status: 200 - Message: API call successful
Errors will be logged similarly:
```

```javascript

2024-11-15 14:01:00 - Status: Error - Message: Request failed: <error_message>
To Check the Log: Open the logs/api_log.txt file.
```

General Notes
Stop the Scripts: Use Ctrl + C for long-running scripts.
Virtual Environment: Ensure the virtual environment is active when running scripts.
Log File: Logs are stored in the logs folder.
