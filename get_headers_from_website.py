import urllib.request
import json

url = input("Enter URL to gather headers from:\n")
http_response = urllib.request.urlopen(url,timeout=60)
if http_response.code == 200:
    print(http_response.headers)
    for key,value in http_response.getheaders(): 
        print(key,value)
else:
    print("Please enter a valid URL using http://www.your_site_here.com")