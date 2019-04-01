# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MlssoccerPipeline(object):

    collection_name = 'mls_players_stg'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # v_items = dict()
        # v_ctr = 0
        # self.db[self.collection_name].insert_one(dict(item))

        for i in zip(item['name'], item['position'], item['jersey_number']):
            self.db[self.collection_name].insert_one({
                'player_name':i[0]
            #     'player_fname':i[0].split(',',0)
            # ,   'player_lname':i[0].split(',',1)
            ,   'position': i[1]
            ,   'jersey_number' : i[2]
            ,   'team_name' : item['team_name'][0]
            ,   'year': item['year'][0]
            })
            # v_ctr = v_ctr + 1
        # return item