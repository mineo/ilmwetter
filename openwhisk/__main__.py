#!/usr/bin/env python
# Copyright © 2017 Wieland Hoffmann
# License: MIT, see LICENSE for details
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from ilmwetter import settings as iw_settings
from ilmwetter.spiders.thedy import ThedySpider

result = None


def item_scraped(item):
    """Handle a scraped item by assigning it to :data:`result`."""
    global result
    result = item


def main(args):
    settings = Settings()
    settings.setmodule(iw_settings)
    spider = ThedySpider()

    process = CrawlerProcess(settings)
    crawler = process.create_crawler(spider)
    crawler.signals.connect(item_scraped,
                            signal=signals.item_scraped)
    process.crawl(crawler)
    process.start(stop_after_crawl=True)
    process.join()

    result["scraping_time"] = result["scraping_time"].isoformat()

    doc = {
        "doc": dict(result)
    }

    return doc


if __name__ == "__main__":
    print main(None)
