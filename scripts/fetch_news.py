import requests

API_KEY = "YOUR_NEWS_API_KEY"

url = f"https://newsapi.org/v2/everything?q=stock market OR finance&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data["articles"]

for article in articles[:5]:
    print(article["title"])
    print(article["description"])
    print()