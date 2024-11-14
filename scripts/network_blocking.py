import requests

BLOCKED_DOMAINS = ["example.com"]

def block_request(url):
    for domain in BLOCKED_DOMAINS:
        if domain in url:
            print(f"Access to {url} is blocked.")
            return {"error": f"Access to {url} is blocked."}
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.json()  # Return the JSON response if successful
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {"error": "Request failed"}

# Test the function
test_url = "https://example.com/test"
result = block_request(test_url)
print("Result:", result)

test_url2 = "https://jsonplaceholder.typicode.com/todos/1"
result2 = block_request(test_url2)
print("Result:", result2)
