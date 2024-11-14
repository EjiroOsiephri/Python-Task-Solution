import os
import requests
from datetime import datetime

def log_api_call(status, message):
    log_directory = "logs"
    log_file_path = f"{log_directory}/api_log.txt"

    # Create the directory if it doesn't exist
    os.makedirs(log_directory, exist_ok=True)

    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now()} - Status: {status} - Message: {message}\n")

def fetch_and_log_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP status errors

        log_api_call(response.status_code, "API call successful")
        
        return response.json()
    except requests.exceptions.RequestException as e:
        log_api_call("Error", str(e))
        print("API request failed:", e)

if __name__ == "__main__":
    data = fetch_and_log_data()
    if data:
        print("Response Data:", data)
