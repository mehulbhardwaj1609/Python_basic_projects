import requests

api_key = "a2d39f604073482da04f6e7f7b05e41a"
query = input("Enter the query: ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-11&sortBy=publishedAt&apiKey={api_key}"

#print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):    #Accessing both index and value during iterationclear
    print(index+1,". ",article["title"], article["url"])
    print("\n----------********-------****-----------------\n")


