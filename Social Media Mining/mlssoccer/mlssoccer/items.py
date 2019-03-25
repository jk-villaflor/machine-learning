# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MlssoccerItem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    jersey_number = scrapy.Field()
    team_name = scrapy.Field()
    pass