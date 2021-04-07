import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem
class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    redis_key = 'yang'

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in tr_list:
            id_num = li.xpath('./span/text()').extract_first()
            title = li.xpath('./span/a/text()').extract_first()
            item = FbsproItem()
            item['id_num'] = id_num
            item['title'] = title
            yield item
