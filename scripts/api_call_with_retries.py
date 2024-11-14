import requests
from requests.exceptions import RequestException

def fetch_data_with_retries():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    attempts = 3

    for attempt in range(1, attempts + 1):
        try:
            print(f"Attempt {attempt} to fetch data...")
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            print("Data fetched successfully!")
            return response.json()  # Return the JSON data if successful
        except RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == attempts:
                raise  # Raise an error after the final failed attempt
            else:
                print("Retrying...")

# Test the function
try:
    data = fetch_data_with_retries()
    print("Response Data:", data)
except Exception as e:
    print("Final Error:", e)
