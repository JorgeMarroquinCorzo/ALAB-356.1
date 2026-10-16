# Requires requests; install with: pip install requests
import requests

# Fetch a URL and print the HTTP status code
url = "https://www.google.com"
response = requests.get(url)

print(f"URL: {url}")
print(f"HTTP Status Code: {response.status_code}")
print(f"Status OK: {response.ok}")  # True if status code is 2xx