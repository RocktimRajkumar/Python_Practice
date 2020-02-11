# Write a program anti_html.py that takes a URL as argument, downloads the html from web
# and print it after stripping html tags.

import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.body
print(soup.text.strip())