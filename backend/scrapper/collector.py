
from get_items_link import get_links
from amazon_scrapper import product_scrapper

links_getter=get_links("computer")
links=links_getter.grab_all_links()


phone_prices=[]
i=0

print(links)

