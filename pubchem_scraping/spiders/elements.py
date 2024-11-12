from typing import Iterable
import scrapy


class ElementsSpider(scrapy.Spider):
    name = "elements"

    def start_requests(self):
         yield scrapy.Request("https://pubchem.ncbi.nlm.nih.gov/ptable/", meta={"playwright": True, "playwright_include_page": True})

    def parse(self, response):
        pass
