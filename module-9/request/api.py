import requests
import json

# API URL for astronauts currently in space
url = "http://api.open-notify.org/astros.json"

# Test the connection
response = requests.get(url)

print("Connection Status Code:", response.status_code)

# Print raw response (no formatting)
print("\nRaw Response:")
print(response.text)

# Convert response to JSON
data = response.json()

print("\nFormatted Astronaut List:")
print("Number of astronauts in space:", data["number"])
print()

for person in data["people"]:
    print(person["name"], "-", person["craft"])