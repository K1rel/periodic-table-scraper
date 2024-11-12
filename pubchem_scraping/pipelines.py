# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class PubchemScrapingPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("elements.db")
        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS periodic_elements (
                            name TEXT,
                            symbol TEXT PRIMARY KEY,
                            atomic_number INTEGER,
                            atomic_mass REAL,
                            chemical_group TEXT
                            );
            """)
        self.conn.commit()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT OR IGNORE INTO periodic_elements VALUES (?, ?, ?, ?, ?)", (
            item["name"],
            item["symbol"],
            item["atomic_number"],
            item["atomic_mass"],
            item["chemical_group"],
        ))
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()