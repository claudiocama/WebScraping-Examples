from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options


url = 'https://www.diretta.it/'
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get(url)
source = driver.page_source
soup = BeautifulSoup(source, "html5lib")
for match in soup.findAll("div", {"class":"event__match"}):
    guest = match.find("div", {"class":"event__participant--home"})
    home = match.find("div", {"class":"event__participant--away"})
    score = match.find("div", {"class":"event__scores"})
    print("{} {} {}".format(guest.text, score.text, home.text))
