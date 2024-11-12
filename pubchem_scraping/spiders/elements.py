from typing import Iterable
import scrapy
from pubchem_scraping.items import ElementItem
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod

class ElementsSpider(scrapy.Spider):
    name = "elements"

    def start_requests(self):
         yield scrapy.Request("https://pubchem.ncbi.nlm.nih.gov/ptable/", meta={"playwright": True,  "playwright_page_methods": [
                PageMethod("wait_for_selector", "div.ptable"),
            ],})

    async def parse(self, response):
        for element in response.css("div.ptable div.element"):
            i = ItemLoader(item=ElementItem(), selector=element)
            i.add_css("name", "[data-tooltip='Name']::text")
            i.add_css("symbol", "[data-tooltip='Symbol']::text")
            i.add_css("atomic_number", "[data-tooltip='Atomic Number']::text")
            i.add_css("atomic_mass", "[data-tooltip*='Atomic Mass']::text")
            i.add_css("chemical_group", "[data-tooltip='Chemical Group Block'] > span::text")

            yield i.load_item()
