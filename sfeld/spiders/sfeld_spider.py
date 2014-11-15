from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import scrapy
from scrapy import Selector 

class SfeldSpider(scrapy.Spider):
	name = "sfeld"
	allowed_domains = ["imdb.com"]
	# start_urls = ["http://www.imdb.com/title/tt0098904/"]
	start_urls = ["http://www.imdb.com/title/tt0098904/episodes?season=1&ref_=tt_eps_sn_1",
	"http://www.imdb.com/title/tt0098904/tvschedule?ref_=tt_wbr_tv"]

	def parse(self, response):
		
		print "in parse"
		
		# import pdb; pdb.set_trace()

		print response.xpath('//h3[@id="episode_top"]/text()').extract()

		print response.css('h3#episode_top').xpath('text()').extract()

		# season = response.xpath('//h3//id=itemprop//@/h3').extract()
		# print season
		# season = sel.xpath(<h3 id="episode_top" itemprop="name"></h3>

		for episode in response.css('div#episodes_content div.list_item'):

			ep_title = episode.css('a[itemprop=name]').xpath('text()').extract()
			print ep_title

			air_date = episode.css('.airdate').xpath('text()').extract()
			print air_date
			
		
			description = episode.css('.item_description').xpath('text()').extract()
			print description
			
		

		# print "parse", ep_title, season, air_date, description, on_tv
			
