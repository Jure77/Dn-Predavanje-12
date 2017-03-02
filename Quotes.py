from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()

prva_stran = BeautifulSoup(html)

quotes = prva_stran.findAll("p", {"class": "quoteContent"})[0:5]
for i in quotes:
    print(i.string)
    print("___________________________________________")