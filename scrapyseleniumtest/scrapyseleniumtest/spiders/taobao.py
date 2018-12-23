from scrapy import Request, Spider
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.baidu.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KWYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)

            yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)
