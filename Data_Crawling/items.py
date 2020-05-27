# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime
#from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst

def float_stars(text):
  return float(text)


class ReviewItem(scrapy.Item):
  Restaurant_Name = scrapy.Field()
  Star = scrapy.Field(input_processor=MapCompose(float_stars),
   output_processor=TakeFirst())
  Review_title = scrapy.Field()            
  Review = scrapy.Field()
  Rating_Date = scrapy.Field()