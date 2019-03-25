# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from mlssoccer.items import MlssoccerItem


class MlsspiderSpider(scrapy.Spider):
    name = 'mlsspider'
    # allowed_domains = ['https://www.mlssoccer.com/rosters/2018/atlanta-united']
    
    def start_requests(self):
        urls = [
            'https://www.mlssoccer.com/rosters/2019/atlanta-united',     
            'https://www.mlssoccer.com/rosters/2019/chicago-fire',          
            'https://www.mlssoccer.com/rosters/2019/fc-cincinnati',         
            'https://www.mlssoccer.com/rosters/2019/colorado-rapids',       
            'https://www.mlssoccer.com/rosters/2019/columbus-crew-sc',      
            'https://www.mlssoccer.com/rosters/2019/fc-dallas',             
            'https://www.mlssoccer.com/rosters/2019/dc-united',             
            'https://www.mlssoccer.com/rosters/2019/houston-dynamo',        
            'https://www.mlssoccer.com/rosters/2019/lafc',                  
            'https://www.mlssoccer.com/rosters/2019/la-galaxy',             
            'https://www.mlssoccer.com/rosters/2019/minnesota-united',      
            'https://www.mlssoccer.com/rosters/2019/montreal-impact',       
            'https://www.mlssoccer.com/rosters/2019/new-england-revolution',
            'https://www.mlssoccer.com/rosters/2019/new-york-city-fc',      
            'https://www.mlssoccer.com/rosters/2019/new-york-red-bulls',    
            'https://www.mlssoccer.com/rosters/2019/orlando-city',          
            'https://www.mlssoccer.com/rosters/2019/philadelphia-union',    
            'https://www.mlssoccer.com/rosters/2019/portland-timbers',      
            'https://www.mlssoccer.com/rosters/2019/real-salt-lake',        
            'https://www.mlssoccer.com/rosters/2019/san-jose-earthquakes',  
            'https://www.mlssoccer.com/rosters/2019/seattle-sounders',      
            'https://www.mlssoccer.com/rosters/2019/sporting-kansas-city',  
            'https://www.mlssoccer.com/rosters/2019/toronto-fc',            
            'https://www.mlssoccer.com/rosters/2019/vancouver-whitecaps',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        v_teamName = response.url.split("/")[-2]
        i = ItemLoader(item=MlssoccerItem(), response=response)
        i.add_xpath("name","//table[@class='activethirty']/tbody/tr/td[@class='playername']/a/text()")
        i.add_xpath("jersey_number","//table[@class='activethirty']/tbody/tr/td[@class='jerseyNum']/text()")
        i.add_xpath("position","//table[@class='activethirty']/tbody/tr/td[@class='position']/text()")
        i.add_value("team_name", v_teamName)
        yield i.load_item()
