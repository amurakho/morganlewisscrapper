# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MorganlevisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    photo_url = scrapy.Field()
    full_name = scrapy.Field()
    position = scrapy.Field()
    phone_numbers = scrapy.Field()
    email = scrapy.Field()
    services = scrapy.Field()
    sectors = scrapy.Field()
    publications = scrapy.Field()
    person_brief = scrapy.Field()
    scrapped_date = scrapy.Field()
