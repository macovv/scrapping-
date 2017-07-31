# -*- coding: utf-8 -*-
import scrapy


class LoggtosSpider(scrapy.Spider):
    name = 'loggtos'
    loggin_url = 'https://logilowice.hekko.pl/dziennik/logowanie.php'
    start_urls = [loggin_url]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response, formdata={'nazwa_uz': 'xxx', 'haslo':'xxx'}, callback = self.parse_sth) 


    def parse_sth(self, response):

        item = {
            'bon': 'cienis',
            'sth': response.css('h1 > span > i::text').extract_first(),
        }
        yield item
        yield scrapy.Request('https://logilowice.hekko.pl/dziennik/u_oceny.php?prz=9&&sem=4', callback=self.parse_test)

    def parse_test(self, response):
        for sth in response.css('td[align=center]'):
            x = sth.css('input::attr(value)').extract_first()
            if not x:
                continue
            else:
                item = {
                    "title":x 
                }
                yield item
