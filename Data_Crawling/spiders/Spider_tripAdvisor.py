#-*- coding: utf-8 -*-


import json
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor 
from scrapy.loader import ItemLoader
from MyThesis.items import ReviewItem
from scrapy.http.request import Request
#create the class of the spider
List_of_Restaurant_Names = []
class ReviewSpider(CrawlSpider):
  name = 'tripAdvisor_crawler'
  allowed_domains = ['tripadvisor.com']
 # start_urls = ['https://www.tripadvisor.com/Restaurants-g187323-Berlin.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g187309-Munich_Upper_Bavaria_Bavaria.html']
  #  start_urls = ['https://www.tripadvisor.com/Restaurants-g187373-Dusseldorf_North_Rhine_Westphalia.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g187291-Stuttgart_Baden_Wurttemberg.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g32655-Los_Angeles_California.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g294217-Hong_Kong.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g35805-Chicago_Illinois.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g255100-Melbourne_Victoria.html']
  #start_urls = ['https://www.tripadvisor.com/Restaurants-g255060-Sydney_New_South_Wales.html']
  start_urls = ['https://www.tripadvisor.com/Restaurants-g294265-Singapore.html']


  

  rules = [Rule(LinkExtractor(allow='/ShowUserReviews-g'),
                  callback='Parse_Review_Trip', follow=True)]
#
#    rules = [Rule(LinkExtractor(allow='/Restaurant_Review'),
#                  callback='Parse_Review_Trip', follow=True)]
#  def Parse_links(self,response):
#    List_of_Restaurant_names = []
#    Restaurant_name = response.css('.HEADING::text').extract()
#    if Restaurant_name not in List_of_Restaurant_names:
#      List_of_Restaurant_names.append(Restaurant_name)
#      yield Request(response.url,callback=self.Parse_Review_Trip, dont_filter=True)
#    else:
#      return (print(*List_of_Restaurant_names, sep = ", "))

  def Parse_Review_Trip(self,response):

    
    
     #in order to take the name of the restaurant for every review
    Restaurant_Name = response.css('.HEADING::text').get()
	
    List_of_Restaurant_Names.append(Restaurant_Name)
    total_reviews=response.css('.is-9')
    for total_review in total_reviews:
#in order to have an outcome if the actual review exist
     if len(total_review.css('.partial_entry::text').extract())!=0:
#in order to have the rating in a more presentable form
       Rating= total_review.css('.ui_bubble_rating::attr(class)').get()
       Star=[Rating[-2:-1] + '.' + Rating[-1:]]
       Review = total_review.css('.quote+ .prw_reviews_text_summary_hsx .partial_entry::text').get()
       Rating_Date = total_review.css('.ratingDate::attr(title)').get()
       Review_title= total_review.css('.noQuotes::text').get()
       loader = ItemLoader(item = ReviewItem())
       loader.add_value('Restaurant_Name' , Restaurant_Name)
       loader.add_value('Star' , Star)
       loader.add_value('Review_title' , Review_title)
       loader.add_value('Review' , Review)
       loader.add_value('Rating_Date' , Rating_Date)
       #print('-----------------------------------------------------------------------------------------------------------------------------------------')
       yield loader.load_item()
     #else:
      # print(response.url)

     