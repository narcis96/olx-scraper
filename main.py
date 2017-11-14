import getpass, sys, scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print (response)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

if __name__ == '__main__':
	#user = input('User: ')
	#password = getpass.getpass()
	#print (user)
	#print (password)
    spider = QuotesSpider()
    for ans in spider.start_requests():
        spider.parse(ans)

