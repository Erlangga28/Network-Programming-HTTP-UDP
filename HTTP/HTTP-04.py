import httplib2
import requests

url = "https://classroom.its.ac.id"

response = requests.get(url)
content_encoding = response.headers.get("Content-Encoding")

print("Content-Type:", response.encoding)