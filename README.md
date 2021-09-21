# thriftshopScraper
 
THRIFTSHOP SCRAPER

WHAT IT IS:

thriftshopScraper scrapes products from three major Korean online secondhand sales websites: 당근마켓(Karrot), 
번개장터(Bunjang), 중고나라(Joongna). 

The user must enter the name of the product they'd like to gather information on, just as they would enter keywords in
the websites' search engines (e.g. "Levi's jeans", "vintage dresses"). Then, the user must specify up to how many items 
they'd like to compare - this is useful because products on page 100 were probably posted years ago, and the seller is 
no longer available. 

WHY I MADE IT:

I love secondhand shops. But because online secondhand sales websites have only recently boomed in Korea, there is no 
price-comparing mechanism to aid thrifters - buyers have to flip through Karrot, Bunjang, and Joongna separately and 
manually compare prices; sellers don't know the equilibrium price and struggle to price their goods. 

Normal online shopping doesn't have this problem; Naver's product aggregator makes it easy for consumers to find the 
best deals. I wanted a product aggregator for online thriftshops, so that is what I am aiming

HOW IT WORKS:

Run thriftshopScraper.py. You will be asked a product to search for - enter a keyword as if you were typing into the
search engine of the thriftshop sites. Then, you must specify the number of items to scrape. You may enter a large 
number; the program will scrape as many items as it can find. 

Once the scraping is completed, you will be asked what information you'd like to analyze: 1) average, 2)
3) minimum, or maximum price. Enter 0 to quit. If you choose to calculate the minimum/maximum, you can then also 
specify how many items you'd like to see - for instance, you should enter "5" to see the top 5 cheapest items. 

THIS PROJECT IS VERY MUCH IN PROGRESS! 
Some functionality I am planning to add:
- Option to scrape all data without having to enter, like, 1000000000. 
Right now, I depend on a for-loop but that shouldn't be the only option.
- Add filtering. Use Selenium to click through each websites' filter options. The issue is that filter buckets are 
different for each site (e.g. Karrot only differentiates "Women's clothes" and "Accessories", but in Bunjang you use 
advanced filters, like "Women's jeans, straight-leg"). Maybe stdout each option and let the user click through each, 
as they would in the actual app.

BUGS:
- CSS class names changing for Bunjang
- "column not found in file" for pandas when 닥터마틴 쿼드 is looked up
