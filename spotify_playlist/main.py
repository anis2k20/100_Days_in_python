from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc=file.read()

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())