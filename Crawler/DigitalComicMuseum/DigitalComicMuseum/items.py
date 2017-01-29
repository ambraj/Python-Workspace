# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ComicItem(Item):
	title = Field()
	rating = Field()
	uploader = Field() # this is the number it is in the list
	downloads = Field()
	publisher = Field()
	series = Field()
	comicMainPageUrl = Field()