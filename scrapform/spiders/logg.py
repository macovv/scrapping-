# -*- coding: utf-8 -*-
import scrapy


class LoggSpider(scrapy.Spider):
    name = 'logg'
    loggin_url = 'http://quotes.toscrape.com/login'
    start_urls = [loggin_url]

    def parse(self, response):
        token = response.css("input[name=csrf_token]::attr(value)").extract_first()
        yield scrapy.FormRequest.from_response(response ,formdata={'csrf_token': token, 'username':'234', 'password':'bb'}, callback = self.parse_quotes)


    def parse_quotes(self, response):
        for q in response.css('div.quote'):
            item = {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first(),
            }
            yield item
