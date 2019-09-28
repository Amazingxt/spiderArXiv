# -*- coding: utf-8 -*-
import scrapy
from arXiv.items import ArxivItem

class QuantumArticleSpider(scrapy.Spider):
    name = 'quantum_article'
    allowed_domains = ['arxiv.com']
    start_urls = ['https://arxiv.org/list/quant-ph/new/']

    def parse(self, response):
        item = ArxivItem()
        for articl_res, url_res in zip(response.xpath('//dd/div[@class="meta"]'),response.xpath('//dt')):
            item['title'] = articl_res.xpath('./div[@class="list-title mathjax"]/text()[2]').extract()[0][:-2]
            abstract = articl_res.xpath('./p[@class="mathjax"]/text()').extract()
            if len(abstract)>0:
                item['abstract'] = articl_res.xpath('./p[@class="mathjax"]/text()').extract()[0]
            else:
                item['abstract'] = None
            item['url'] = 'https://arxiv.org' + url_res.xpath('./span/a[@title="Download PDF"]/@href').extract()[0]
            yield item
