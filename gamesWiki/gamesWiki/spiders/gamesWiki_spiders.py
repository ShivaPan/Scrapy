import scrapy
from scrapy import Spider
from gamesWiki.items import GameswikiItem

class gamesWikiSpider(Spider):
	name = 'gamesWiki'
	allowed_urls = ['https://en.wikipedia.org/']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_Super_Nintendo_Entertainment_System_games'] #update the url with the wiki page that will be pulled

	def parse(self,response):


		rows = response.xpath('//*[@id="mw-content-text"]/div/table//tr')
		#rows = response.xpath('//*[@id="mw-content-text"]/div/table//')

		#ps
		#rows = response.xpath('//*[@id="mw-content-text"]/div/ul[1]/li')

		for row in rows:

			#playstation

			#title = row.xpath('./i/a/text()').extract_first()
			#sales = row.xpath('./text()').extract_first()

			#The list below is updated depending on the given wikipedia table

			title = row.xpath('./td[1]/i/a/text()').extract_first()
			developer = row.xpath('./td[6]/a/text()').extract_first()
			sales = row.xpath('./td[2]/span/text()').extract_first()
			release = row.xpath('./td[4]/ul/li[1]/text()').extract_first()
			publisher = row.xpath('./td[7]/text()').extract_first()
			release = row.xpath('.//span[@style="white-space:nowrap"]/text()').extract_first()
			genre = row.xpath('./td[5]/a/text()').extract_first()



			item = GameswikiItem()
			item['title'] = title
			item['developer'] = developer
			item['sales'] = sales
			item['publisher'] = publisher
			item['release'] = release
			genre['genre'] = genre
			yield item

