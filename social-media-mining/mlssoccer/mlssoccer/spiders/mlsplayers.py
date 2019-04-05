# -*- coding: utf-8 -*-
import scrapy


class MlsplayersSpider(scrapy.Spider):
    name = 'mlsplayers'
    # allowed_domains = ['https://www.mlssoccer.com/players?site_path=players']

    def start_requests(self):
        urls = ['https://www.mlssoccer.com/players?site_path=players&position=All&club=All&status=A']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        i = ItemLoader(item=MlsplayersItem(), response=response)
        i.add_xpath("name","//table[@class='activethirty']/tbody/tr/td[@class='playername']/a/text()")
        i.add_xpath("jersey_number","//table[@class='activethirty']/tbody/tr/td[@class='jerseyNum']/text()")
        i.add_xpath("position","//table[@class='activethirty']/tbody/tr/td[@class='position']/text()")
        i.add_value("team_name", response.url.split("/")[-1])
        i.add_value("year",response.url.split("/")[-2])
        yield i.load_item()