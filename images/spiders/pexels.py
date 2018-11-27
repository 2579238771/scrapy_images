# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagesItem

class PexelsSpider(CrawlSpider):
    name = 'pexels'
    allowed_domains = ['pexels.com']
    start_urls = ['https://www.pexels.com/search/display/']

    rules = (
        Rule(LinkExtractor(allow=r'^https://www.pexels.com/photo/.*/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ImagesItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['file_urls'] = response.xpath('.//img[contains(@src,"https://")]/@src').extract()
        # print(i)
        return i