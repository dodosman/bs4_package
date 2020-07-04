import requests
from bs4 import BeautifulSoup

def get_text():
    user_url = input("What page do you wan't to webscrape?: ")
    URL = user_url

    # get html page
    page = requests.get(URL)

    # get the html code
    soup = BeautifulSoup(page.content, 'html.parser')
    # prints page's texts from inserted page

    for paraph in soup.find_all('a'):
        print(soup.get_text())

