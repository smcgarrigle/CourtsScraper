# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CourtscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	url= scrapy.Field()
	title= scrapy.Field()
	headerh1= scrapy.Field()
	dv= scrapy.Field()
	content= scrapy.Field()
	htmlcontent= scrapy.Field()
