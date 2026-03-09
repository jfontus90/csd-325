import requests

# API that returns astronauts currently in space
url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

data = response.json()

print("Number of astronauts currently in space:", data["number"])
print()

for person in data["people"]:
    print(person["name"], "-", person["craft"])