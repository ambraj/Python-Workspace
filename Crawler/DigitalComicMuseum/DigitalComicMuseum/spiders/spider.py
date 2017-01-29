import scrapy
from DigitalComicMuseum.items import ComicItem

class tutorialSpider(scrapy.Spider):
	name = "tutorial"
	allowed_domains = ["digitalcomicmuseum.com"]
	start_urls = [
		"http://digitalcomicmuseum.com/stats.php?ACT=topdl&start=0&limit=10"
	] 

	def parse(self, response):
		self.wanted_num=10
		for sel in response.xpath("//*[@class='mainrow']"):
			item = ComicItem()
			item['title'] = sel.xpath('td[1]/table/tr/td[2]/a/text()').extract()[0]
			item['rating'] = sel.xpath('td[5]/div/text()').extract()[0]
			item['uploader'] = sel.xpath('td[2]/div/text()').extract()[0]
			item['downloads'] = sel.xpath('td[6]/div/text()').extract()[0]
			item['comicMainPageUrl'] = sel.xpath('td[1]/table/tr/td[2]/a/@href').extract()[0]

			request = scrapy.Request(item['comicMainPageUrl'], callback=self.parseComicDetails)
			request.meta['item'] = item
			yield request
			
	def parseComicDetails(self, response):
		print('parsing comic.......')
		item = response.meta['item']
		item['publisher'] = response.xpath("//*[@class='nav']/b/a/text()").extract()[1]
		item['series'] = response.xpath("//*[@class='nav']/b/a/text()").extract()[2]

		print('\n************\n')
		print(item)
		print('\n************\n')

		return item