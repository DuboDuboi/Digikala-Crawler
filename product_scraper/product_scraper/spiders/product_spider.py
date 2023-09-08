import scrapy
import json
import pandas as pd
import requests
from random import randint

class ProductSpider(scrapy.Spider):
    name = 'product'
    # start_urls = ['https://api.digikala.com/v1/product/10890061/']

    # #add random headers list
    

    # def get_headers_list():
    #     SCRAPEOPS_API_KEY = 'cd6b7fda-abcc-47ae-89f8-0596b8668aed'
    #     response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + SCRAPEOPS_API_KEY)
    #     json_response = response.json()
    #     return json_response.get('result', [])

    # def get_random_header(header_list):
    #     random_index = randint(0, len(header_list) - 1)
    #     return header_list[random_index]

    # header_list = get_headers_list()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
    }

    
    def start_requests(self):
        with open('F:\Machine Learning\Digikala Scrapper\Python-Crawler\product_scraper\product_scraper\productsdetails.json', 'r') as json_file:
            json_data = json.load(json_file)

        # Extract product IDs from the JSON data
        json_product_ids = {int(item['id'][0]) if isinstance(item['id'], list) else int(item['id']) for item in json_data}

        df = pd.read_csv('F:\Machine Learning\Digikala Scrapper\Python-Crawler\Scraped\products.csv')
        product_codes = df['product_id']

        # Filter product IDs that are not in the JSON data
        filtered_product_codes = [code for code in product_codes if code not in json_product_ids]

        # headers = self.get_random_header()
        # df =pd.read_csv('F:\Machine Learning\Digikala Scrapper\Python-Crawler\Scraped\products.csv')
        # product_codes = df['product_id']
        for code in filtered_product_codes:
            yield scrapy.Request(f'https://api.digikala.com/v1/product/{code}/', headers=self.headers, callback=self.parse)

    def parse(self, response):
        try:
            data = json.loads(response.text)
            try:
                product = data.get('data', {}).get('product', {})
            except:
                id_pro = response.url.split('/')[-2]

            try:
                also_bought = data.get('data', {}).get('recommendations', {}).get('also_bought_products', {}).get("products", [])
            except:
                also_bought = None

            try:
                related = data.get('data', {}).get('recommendations', {}).get('related_products', {}).get("products", [])
            except:
                related = None

            # if product.get('id') == 10890061:
            try:
                also_bought_product_ids = [p.get('id') for p in also_bought]
            except:
                also_bought_product_ids = None
            try:
                related_product_ids = [p.get('id') for p in related]
            except:
                related_product_ids = None

            try:
                id_pro = product.get('id'),
            except:
                id_pro = None

            try:
                title_fa = product.get('title_fa'),
            except:
                title_fa = None

            try:
                title_en = product.get('title_en'),
            except:
                title_en = None

            try:
                status = product.get('status'),
            except:
                status = None

            try:
                brand = product.get('data_layer', {}).get('brand'),
            except:
                brand = None

            try:
                brand_category = product.get('data_layer', {}).get('category'),
            except:
                brand_category = None

            try:
                score = product.get('data_layer', {}).get('dimension9'),
            except:
                score = None


            try:
                suggestion_percentage = product.get('suggestion', {}).get('percentage'),
            except:
                suggestion_percentage = None

            try:
                suggestion_count = product.get('suggestion', {}).get('count'),
            except:
                suggestion_count = None


            try:
                item_category2 = product.get('data_layer', {}).get('item_category2'),
            except:
                item_category2 = None

            try:
                item_category3 = product.get('data_layer', {}).get('item_category3'),
            except:
                item_category3 = None

            try:
                item_category4 = product.get('data_layer', {}).get('item_category4'),
            except:
                item_category4 = None

            try:
                item_category5 = product.get('data_layer', {}).get('item_category5'),
            except:
                item_category5 = None

            try:
                item_category6 = product.get('data_layer', {}).get('item_category6'),
            except:
                item_category6 = None

            try:
                item_category7 = product.get('data_layer', {}).get('item_category7'),
            except:
                item_category7 = None

            try:
                item_category8 = product.get('data_layer', {}).get('item_category8'),
            except:
                item_category8 = None

            try:
                item_category9 = product.get('data_layer', {}).get('item_category9'),
            except:
                item_category9 = None

            try:
                item_category10 = product.get('data_layer', {}).get('item_category10'),
            except:
                item_category10 = None

            try:
                item_category11 = product.get('data_layer', {}).get('item_category11'),
            except:
                item_category11 = None

            try:
                item_category12 = product.get('data_layer', {}).get('item_category12'),
            except:
                item_category12 = None

            try:
                item_category13 = product.get('data_layer', {}).get('item_category13'),
            except:
                item_category13 = None

            try:
                item_category14 = product.get('data_layer', {}).get('item_category14'),
            except:
                item_category14 = None

            try:
                item_category15 = product.get('data_layer', {}).get('item_category15'),
            except:
                item_category15 = None

            

            try:
                seller_id = product.get('default_variant', {}).get('seller', {}).get('id')
            except:
                seller_id = None
            
            try:
                seller_title = product.get('default_variant', {}).get('seller', {}).get('title'),
            except:
                seller_title = None

            try:
                seller_code = product.get('default_variant', {}).get('seller', {}).get('code'),
            except:
                seller_code = None

            try:
                seller_url = product.get('default_variant', {}).get('seller', {}).get('url'),
            except:
                seller_url = None

            try:
                seller_total_rate = product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('total_rate'),
            except:
                seller_total_rate = None

            try:
                seller_total_count = product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('total_count'),
            except:
                seller_total_count = None

            try:
                seller_grade = product.get('default_variant', {}).get('seller', {}).get('grade', {}).get('label'),
            except:
                seller_grade = None

            try:
                seller_commitment = product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('commitment'),
            except:
                seller_commitment = None

            try:
                seller_no_return = product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('no_return'),
            except:
                seller_no_return = None

            try:
                seller_on_time_shipping = product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('on_time_shipping'),
            except:
                seller_on_time_shipping = None
            
            try:
                selling_price = product.get('default_variant', {}).get('price', {}).get('selling_price'),
            except:
                selling_price = None
                
            try:
                rrp_price = product.get('default_variant', {}).get('price', {}).get('rrp_price'),
            except:
                rrp_price = None

            try:
                order_limit = product.get('default_variant', {}).get('price', {}).get('order_limit'),
            except:
                order_limit = None

            try:
                is_incredible = product.get('default_variant', {}).get('price', {}).get('is_incredible'),
            except:
                is_incredible = None

            try:
                is_promotion = product.get('default_variant', {}).get('price', {}).get('is_promotion'),
            except:
                is_promotion = None

            try:
                discount_percent = product.get('default_variant', {}).get('price', {}).get('discount_percent'),
            except:
                discount_percent = None


            try:
                review = product.get('review', {}).get('attributes', {}),
            except:
                review = None

            try:
                product_advantages = product.get('pros_and_cons', {}).get('advantages'),
            except:
                product_advantages = None

            try:
                product_disadvantages = product.get('pros_and_cons', {}).get('disadvantages'),
            except:
                product_disadvantages = None
                
            try:
                category_id = product.get('category', {}).get('id'),
            except:
                category_id = None

            try:
                category_title_fa = product.get('category', {}).get('title_fa'), 
            except:
                category_title_fa = None

            try:                   
                category_title_en = product.get('category', {}).get('title_en'),
            except:
                category_title_en = None

            try:
                also_bought_product_ids = also_bought_product_ids,
            except:
                also_bought_product_ids = None

            try:
                related_product_ids = related_product_ids,
            except:
                related_product_ids = None


            yield {
                'id': id_pro,
                'title_fa': title_fa,
                'title_en': title_en,
                'status': status,
                'brand': brand,
                'brand_category': brand_category,
                'score': score,

                'suggestion_percentage': suggestion_percentage,
                'suggestion_count': suggestion_count,

                'item_category2': item_category2,
                'item_category3': item_category3,
                'item_category4': item_category4,
                'item_category5': item_category5,
                'item_category6': item_category6,
                'item_category7': item_category7,
                'item_category8': item_category8,
                'item_category9': item_category9,
                'item_category10': item_category10,
                'item_category11': item_category11,
                'item_category12': item_category12,
                'item_category13': item_category13,
                'item_category14': item_category14,
                'item_category15': item_category15,

                'seller_id': seller_id,
                'seller_title': seller_title,
                'seller_code': seller_code,
                'seller_url': seller_url,
                'seller_total_rate': seller_total_rate,
                'seller_total_count': seller_total_count,
                'seller_grade': seller_grade,
                'seller_commitment': seller_commitment,
                'seller_no_return': seller_no_return,
                'seller_on_time_shipping': seller_on_time_shipping,

                'selling_price': selling_price,
                'rrp_price': rrp_price,
                'order_limit': order_limit,
                'is_incredible': is_incredible,
                'is_promotion': is_incredible,
                'discount_percent': discount_percent,

                'review': review,
                'product_advantages': product_advantages,
                'product_disadvantages': product_disadvantages,
                
                'category_id': category_id,
                'category_title_fa': category_title_fa,
                'category_title_en': category_title_en,

                'also_bought_product_ids': also_bought_product_ids,
                'related_product_ids': related_product_ids,
            }

        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decoding error: {e}")
            # If there's an error, add the ID to the error_ids list and save it to a JSON file
            product_id = response.url.split('/')[-2]
            error_ids = [product_id]

            # Check if the JSON file exists
            try:
                with open('error_ids.json', 'r') as error_file:
                    existing_error_ids = json.load(error_file)
                    error_ids.extend(existing_error_ids)
            except (FileNotFoundError, json.JSONDecodeError):
                pass

            with open('error_ids.json', 'w') as error_file:
                json.dump(error_ids, error_file, ensure_ascii=False, indent=4)
  