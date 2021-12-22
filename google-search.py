from googlesearch import search

print("Welcome to Google Search")

query = input("What do you want to search on google?  ")

for i in search(query, start=0, stop=6):

    print(i)
