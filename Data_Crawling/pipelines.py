# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
import json
	

class DuplicatesPipeline(object):

  def __init__(self):
    self.reviews_seen = set()
	
  def process_item(self, item, spider): 
    if item['Review'][0] in self.reviews_seen: 
      raise DropItem("Repeated items found: %s" % item) 
    else: 
      self.reviews_seen.add(item['Review'][0]) 
      return item
	
	
	
class JsonWriterPipeline(object):


	def open_spider(self, spider):
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Berlin.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Munich.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Dusseldorf.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Stuttgard.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_New_York.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Los_Angeles.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_London.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Hong_Kong.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Chicago.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Melbourne.json', 'w')
		#self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Sydney.json', 'w')
		self.file = open('/root/mythesis/MyThesis/MyThesis/Crawled_Data/TripAdvisor_crawled_Singapore.json', 'w')
		

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		line = json.dumps(dict(item),ensure_ascii=False) + "\n"
		self.file.write(line)
		return item
