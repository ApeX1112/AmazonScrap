import time
from scrapper import amazon_scrapper

def background_task():
    from .models import product,priceUpdate
    while True:
        try:
            products = product.objects.all()
            try:
                for prod in products:
                    url=prod.url
                    productname=prod.name
                    productscrapper=amazon_scrapper.product_scrapper(url)
                    current_price=productscrapper.get_price()

                    priceUpdate.objects.create(
                        price=current_price,
                        productName=prod,
                        
                    )

                    print(f'-------{productname}------- has been tracked ...')
            except Exception as inner_exception:
                print (f"Failed to track {prod.name}: {inner_exception}")
            time.sleep(10)
        except Exception as e:
            print(f"Error in background_task: {e}")
            time.sleep(10)