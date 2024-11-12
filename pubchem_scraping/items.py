import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class ElementItem(scrapy.Item):
    
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags , str.strip),
        output_processor = TakeFirst()
    )
    symbol = scrapy.Field(
        input_processor = MapCompose(remove_tags , str.strip),
        output_processor = TakeFirst()
    )
    atomic_number = scrapy.Field(
        input_processor = MapCompose(remove_tags , str.strip, int),
        output_processor = TakeFirst()
        )
    atomic_mass = scrapy.Field(
        put_processor = MapCompose(remove_tags , str.strip, float),
        output_processor = TakeFirst()
        )
    chemical_group = scrapy.Field(
        dinput_processor = MapCompose(remove_tags , str.strip),
        output_processor = TakeFirst()
        )
    pass
