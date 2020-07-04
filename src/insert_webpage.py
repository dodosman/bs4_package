import requests
from bs4 import BeautifulSoup

def url_input():
    user_url = input("What page do you wan't to webscrape?: ")
    URL = user_url

    #get html page
    page = requests.get(URL)

    #get the html code
    soup = BeautifulSoup(page.content, 'html.parser')
    #prints page's html code
    print(soup.prettify())