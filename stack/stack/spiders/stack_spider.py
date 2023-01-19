from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem
import time
import random
from datetime import datetime

class StackSpider(Spider):
    name = 'stack'
    allowed_domains = ["markets.businessinsider.com"]
    start_urls = [
        r"https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=shortterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19",
        r"https://markets.businessinsider.com/bonds/finder?p=2&borrower=71&maturity=shortterm&bondtype=2%2c3%2c4%2c16&currency=184&country=19",
        r"https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=midterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19"
    ]

    def parse(self, response):
        bonds = Selector(response).xpath('//tbody[@class="table__tbody"]/tr')

        for bond in bonds:
            time.sleep(random.randint(0,4))
            item = StackItem()
            item['bid'] = "".join(bond.xpath('./td[7]/text()').extract()[0].split())
            item['ask'] = "".join(bond.xpath('./td[8]/text()').extract()[0].split())
            item['maturity_date'] = "".join(bond.xpath('./td[6]/text()').extract()[0].split())
            item['maturity_date'] = datetime.strptime(item['maturity_date'], r"%m/%d/%Y")
            item['bond_yield'] = "".join(bond.xpath('./td[4]/text()').extract()[0].split())
            item['coupon'] = "".join(bond.xpath('./td[3]/text()').extract()[0].split())
            item['name'] = f"CAN {item['coupon'][:4]} {item['maturity_date'].strftime(r'%b')} {item['maturity_date'].year % 2000}" #need to edit the date
            yield item
