# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from mlssoccer.items import MlslistItem


class MlslistSpider(scrapy.Spider):
    name = 'mlslist'

    def start_requests(self):
        urls = ['https://www.mlssoccer.com/players']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # i = ItemLoader(item=MlslistItem(), response=response)
        # i.add_xpath("url","response.xpath('//a[@class='name_link']/@href')")
        # yield i.load_item()

        for sel in response.xpath("//a[@class='name_link']/@href"):
            item = MlslistItem()
            item['url'] = sel.get()
        yield item