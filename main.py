import getpass, sys, scrapy
import urllib.request, requests
from bs4 import BeautifulSoup
import re
import smtplib

class Scraper():
    def __init__(self, url):
        self.__page = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')

    def GetContent(self, str, tag, atStop):
        links = []
        starts =[m.start() for m in re.finditer(tag, str)]
        for start in starts:
            stop = str.find(atStop, start + 1)
            links.append(str[start + len(tag):stop])
        return links

    def GetCategories(self):
        categories = ''
        for item in self.__page.find_all('div', attrs={'class': 'maincategories-list clr'}):
            categories = categories  + str(item)
        links = self.GetContent(categories, "href=\"", '">')
        names = self.GetContent(categories, "<span>", '<')
        return list(zip(names,links))

    def GetSubcategories(self, category):
        subcategories = ''
        for item in self.__page.find_all('div', attrs={'class': 'subcategories-list clr'}):
            subcategories = subcategories  + str(item)
        fromPos = subcategories.find(category + '\t')
        to = subcategories.find("link inlblk", fromPos)
        subcategories = subcategories[fromPos:to]
        #print(subcategories)
        links = self.GetContent(subcategories, "href=\"", '">')
        names = self.GetContent(subcategories, "<span>", '<')
        return list(zip(names,links))

if __name__ == '__main__':
    user = 'boss'#input('User: ')
    password = 'boss'#getpass.getpass()
    city = 'bucuresti'#input('Oras: ')
    scraper = Scraper('https://www.olx.ro/')
    categories = scraper.GetCategories()
    for i, (categoryName, categoryLink) in enumerate(categories):
        print(i, categoryName)
    category = int(input('Categories [0 - ' + str(len(categories) - 1) + ']: '))
    subcategories = scraper.GetSubcategories(categories[category][0])
    for i, (subcategoryName, subcategoryLink) in enumerate(subcategories):
        print(i, subcategoryName, subcategoryLink)
    subcategory = int(input('Subcategories [0 - ' + str(len(subcategories) - 1) + ']: '))
    print(subcategories[subcategory][1])
    print('here')
    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.starttls()
    print('and ... here')
    server.login("user", "pass")
    msg = "Hello!" # The /n separates the message from the headers
    server.sendmail("you@gmail.com", "target@example.com", msg)
    #print (user)
	#print (password)

