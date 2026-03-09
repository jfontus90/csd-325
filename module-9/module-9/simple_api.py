import requests

# Simple API that predicts age from a name
url = "https://api.agify.io/?name=jasmine"

response = requests.get(url)

print("Status Code:", response.status_code)
print()

# Print raw response (no formatting)
print("Raw Response:")
print(response.text)
print()

# Print formatted response
data = response.json()

print("Formatted Output:")
print("Name:", data["name"])
print("Predicted Age:", data["age"])
print("Count:", data["count"])