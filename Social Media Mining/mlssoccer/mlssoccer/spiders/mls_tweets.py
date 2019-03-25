# -*- coding: utf-8 -*-
import scrapy


class MlsTweetsSpider(scrapy.Spider):
    name = 'mls_tweets'
    allowed_domains = ['https://twitter.com/hashtag/mlsallstar?lang=en']
    start_urls = ['http://https://twitter.com/hashtag/mlsallstar?lang=en/']

    def parse(self, response):
        pass
