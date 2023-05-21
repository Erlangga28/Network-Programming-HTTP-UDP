from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://classroom.its.ac.id').read()

soup = BeautifulSoup(response, features="lxml")

print(soup.title.string)
print(soup.get_text())