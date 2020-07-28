import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from datetime import datetime

from morganlevis.items import MorganlevisItem


class MorganSpider(scrapy.Spider):
    name = 'morgan'
    base_url = 'https://www.morganlewis.com/api/custom/peoplesearch/search?keyword=&category=bb82d24a9d7a45bd938533994c4e775a&sortBy=lastname' \
               '&pageNum={page_number}' \
               '&numberPerPage={number_per_page}' \
               '&numberPerSection=5&enforceLanguage=&languageToEnforce=&school=&position=&location=&court=&judge=&isFacetRefresh=true'
    start_urls = [
        base_url.format(page_number=1, number_per_page=1)
    ]

    def parse(self, response):
        if not response.meta.get('total_pages'):
            total_pages = int(response.css('.c-results__listing').attrib['data-total'])
            url = self.base_url.format(page_number=1, number_per_page=total_pages)
            yield scrapy.Request(url, meta={'total_pages': total_pages})
        else:
            links = LinkExtractor(allow='bios/', deny=r'p=[0-9]$').extract_links(response)
            yield from response.follow_all(links, callback=self.parse_bio)

    def parse_bio(self, response):
        item = MorganlevisItem()
        item['url'] = response.url
        item['photo_url'] = response.xpath('.//img[@itemprop="image"]').attrib['src']
        item['full_name'] = response.xpath('.//span[@itemprop="name"]/text()').get()
        item['position'] = response.css('.person-heading h2::text').get()
        item['phone_numbers'] = response.xpath('.//p[@itemprop="telephone"]/a/text()').getall()
        item['email'] = response.xpath('.//a[@itemprop="email"]/text()').get()
        item['services'] = response.css('.person-depart-info:contains("Services") a::attr(title)').getall()
        item['sectors'] = response.css('.person-depart-info:contains("Sectors") a::attr(title)').getall()
        item['person_brief'] = response.css('.purple-para p::text').get()
        item['scrapped_date'] = datetime.now().date()

        item_id = response.css('script:contains("itemId")').re_first('itemId: "(.*)"')
        formdata ={
              "itemID": item_id,
              "itemType": "publicationitemlist",
              "printView": ""
            }
        add_url = 'https://www.morganlewis.com/api/sitecore/accordion/getaccordionlist'
        yield FormRequest(add_url, formdata=formdata, callback=self.add_block_parse, meta={'item': item})

    def add_block_parse(self, response):
        item = response.meta['item']
        item['publications'] = response.css('a::attr(title)').getall()
        return item