import json
import requests

#Get user input
keyword = input('Enter what you would like to search for: ')

#Apply input into url that fetches posts with that keyword in UMD's subreddit
#Only the author, title, and link are extracted
url = f'https://api.pushshift.io/reddit/search/submission/?q="{keyword}"&filter=title,author,full_link&subreddit=umd'
info = requests.get(url).json()

#Open a file to write to, then write into it, and close it
jsonFile = open('results.json', 'w')
json.dump(info, jsonFile, indent = 2, sort_keys=True)
jsonFile.close()