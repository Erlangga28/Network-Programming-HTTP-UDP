import httplib2
import requests

response = requests.get("https://www.its.ac.id")

print("Content-Encoding:", response.headers['Content-Encoding'])

