#requests library for requesting webpages
import requests

#creating url variable to hold the url of the webpage I want to scrape
url = "https://www.amazon.com/bestsellers/books/"

#using the get function from the requests library to return the contents of url
page = requests.get(url)

#using .text to display the contents of page and save to a variable called contents, then print
contents = page.text
print(contents)

#importing BeautifulSoup
from bs4 import BeautifulSoup

#running contents through BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')

print(soup.get_text())
