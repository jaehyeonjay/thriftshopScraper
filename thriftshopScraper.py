import dataInterpreter
import inputHandler
import karrotScraper
import bunjangScraper
import joongnaScraper


def open_file():
    db = open("thriftshopScraperData.txt", "x")
    db.write("SHOP\tITEM\tPRICE\n")
    return db


def dispatch_scrapers(keyword, nitems, db):
    print("SCRAPING KARROT...")
    karrotScraper.scrape_karrot(keyword, nitems, db)
    print("SCRAPING BUNJANG...")
    bunjangScraper.scrape_bunjang(keyword, nitems, db)
    print("SCRAPING JOONGNA...")
    joongnaScraper.scrape_joongna(keyword, nitems, db)


argv = inputHandler.get_seed_input()
db = open_file()
dispatch_scrapers(argv[0], argv[1], db)
while True:
    if not dataInterpreter.task_handler(db.name):
        break
db.close()