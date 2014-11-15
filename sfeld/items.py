# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SfeldItem(scrapy.Item):
  	season = scrapy.Field()
	ep_title = scrapy.Field()
	air_date = scrapy.Field()
	description = scrapy.Field()
	on_tv = scrapy.Field()
