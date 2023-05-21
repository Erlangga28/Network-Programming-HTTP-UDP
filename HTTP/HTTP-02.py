import httplib2
import requests

url = "https://its.ac.id"

response = requests.get(url)
content_encoding = response.headers.get("Content-Encoding")

print("Content-Encoding:", content_encoding)