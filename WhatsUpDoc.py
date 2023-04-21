import requests
import json

# Enter your News API key here
api_key = "YOUR_API_KEY"

# Define the API endpoint and parameters
url = "https://newsapi.org/v2/top-headlines"
params = {
    "q": "cybersecurity",
    "category": "technology",
    "country": "us",
    "pageSize": 10,
    "apiKey": api_key
}

# Send a GET request to the API and parse the response as JSON
response = requests.get(url, params=params)
data = json.loads(response.text)

# Iterate through each article and print its title and description
for article in data["articles"]:
    print("-" * 50)
    print(article["title"])
    print(article["description"])
    print(article["url"])
