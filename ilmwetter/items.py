# -*- coding: utf-8 -*-
import scrapy


class IlmwetterItem(scrapy.Item):
    scraping_time = scrapy.Field()
    temperature = scrapy.Field()
    humidity = scrapy.Field()
    dew_point = scrapy.Field()
    pressure = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_speed = scrapy.Field()
    solar_radiation = scrapy.Field()
    precipitation_amount = scrapy.Field()
