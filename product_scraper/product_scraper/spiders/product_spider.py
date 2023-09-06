import scrapy
import json

class ProductSpider(scrapy.Spider):
    name = 'product'
    start_urls = ['https://api.digikala.com/v1/product/10890061/']

    # Add custom headers
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        try:
            data = json.loads(response.text)
            product = data.get('data', {}).get('product', {})
            also_bought = data.get('data', {}).get('recommendations', {}).get('also_bought_products', {}).get("products", [])
            related = data.get('data', {}).get('recommendations', {}).get('related_products', {}).get("products", [])

            if product.get('id') == 10890061:

                also_bought_product_ids = [p.get('id') for p in also_bought]
                related_product_ids = [p.get('id') for p in related]


                yield {
                    'id': product.get('id'),
                    'title_fa': product.get('title_fa'),
                    'title_en': product.get('title_en'),
                    'status': product.get('status'),
                    'brand': product.get('data_layer', {}).get('brand'),
                    'brand_category': product.get('data_layer', {}).get('category'),
                    'score': product.get('data_layer', {}).get('dimension9'),

                    'suggestion_percentage': product.get('suggestion', {}).get('percentage'),
                    'suggestion_count': product.get('suggestion', {}).get('count'),

                    'item_category2': product.get('data_layer', {}).get('item_category2'),
                    'item_category3': product.get('data_layer', {}).get('item_category3'),
                    'item_category4': product.get('data_layer', {}).get('item_category4'),
                    'item_category5': product.get('data_layer', {}).get('item_category5'),
                    'item_category6': product.get('data_layer', {}).get('item_category6'),
                    'item_category7': product.get('data_layer', {}).get('item_category7'),
                    'item_category8': product.get('data_layer', {}).get('item_category8'),
                    'item_category9': product.get('data_layer', {}).get('item_category9'),
                    'item_category10': product.get('data_layer', {}).get('item_category10'),
                    'item_category11': product.get('data_layer', {}).get('item_category11'),
                    'item_category12': product.get('data_layer', {}).get('item_category12'),
                    'item_category13': product.get('data_layer', {}).get('item_category13'),
                    'item_category14': product.get('data_layer', {}).get('item_category14'),
                    'item_category15': product.get('data_layer', {}).get('item_category15'),
                    
                    'seller_id': product.get('default_variant', {}).get('seller', {}).get('id'),
                    'seller_title': product.get('default_variant', {}).get('seller', {}).get('title'),
                    'seller_code': product.get('default_variant', {}).get('seller', {}).get('code'),
                    'seller_url': product.get('default_variant', {}).get('seller', {}).get('url'),
                    'seller_total_rate': product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('total_rate'),
                    'seller_total_count': product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('total_count'),
                    'seller_grade': product.get('default_variant', {}).get('seller', {}).get('grade', {}).get('label'),
                    'seller_commitment': product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('commitment'),
                    'seller_no_return': product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('no_return'),
                    'seller_on_time_shipping': product.get('default_variant', {}).get('seller', {}).get('rating', {}).get('on_time_shipping'),

                    'selling_price': product.get('default_variant', {}).get('price', {}).get('selling_price'),
                    'rrp_price': product.get('default_variant', {}).get('price', {}).get('rrp_price'),
                    'order_limit': product.get('default_variant', {}).get('price', {}).get('order_limit'),
                    'is_incredible': product.get('default_variant', {}).get('price', {}).get('is_incredible'),
                    'is_promotion': product.get('default_variant', {}).get('price', {}).get('is_promotion'),
                    'discount_percent': product.get('default_variant', {}).get('price', {}).get('discount_percent'),

                    'review': product.get('review', {}).get('attributes', {}),
                    'product_advantages': product.get('pros_and_cons', {}).get('advantages'),
                    'product_disadvantages': product.get('pros_and_cons', {}).get('disadvantages'),
                    
                    'category_id': product.get('category', {}).get('id'),
                    'category_title_fa': product.get('category', {}).get('title_fa'),
                    'category_title_en': product.get('category', {}).get('title_en'),

                    'also_bought_product_ids': also_bought_product_ids,
                    'related_product_ids': related_product_ids,
                }

        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decoding error: {e}")