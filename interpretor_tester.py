import dataInterpreter
import inputHandler

db = open("thriftshopScraperData.txt", "r")
#n_total_items = int(input("MANUALLY ENTER TOTAL NUMBER OF ITEMS SCRAPED: "))
while True:
    if not dataInterpreter.task_handler(db.name):
        break
db.close()