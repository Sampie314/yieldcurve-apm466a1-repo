# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    name = scrapy.Field()
    maturity_date = scrapy.Field()
    bond_yield = scrapy.Field()
    coupon = scrapy.Field()
    url = scrapy.Field()


