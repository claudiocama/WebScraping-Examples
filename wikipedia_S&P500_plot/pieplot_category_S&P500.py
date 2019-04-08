from bs4 import BeautifulSoup
import requests
from collections import Counter
from textwrap import wrap
import matplotlib.pyplot as plt

response = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = BeautifulSoup(response.text, "html5lib")
table = soup.find("table", {"class":"wikitable sortable"})
list_of_sp500 = []

for row in table.findAll("tr")[1:]:
    list_of_sp500.append(row.findAll("td")[3].text)

counts = Counter(list_of_sp500)
plt.figure(figsize=(10,10))
plt.pie([int(v) for v in counts.values()], labels=[ '\n'.join(wrap(l, 20)) for l in counts])
plt.show()
