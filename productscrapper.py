import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import csv
import re
import pyppeteer_stealth

def persian_to_english(text):
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    translation = str.maketrans(persian_digits, english_digits)
    return text.translate(translation)

def extract_product_id(url):
    match = re.search(r'/product/dkp-(\d+)/', url)
    if match:
        return match.group(1)
    return None

async def main():
    browser = await launch({"headless": True})
    page = await browser.newPage()
    await pyppeteer_stealth.stealth(page)  # Apply pyppeteer-stealth

    i = 0 

    with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the header row
        csvwriter.writerow(['page_id', 'product_id', 'product_name', 'product_price', 'product_rating', 'product_link'])

        # Iterate through 500 pages
        for page_number in range(1, 3):  # Assuming you want to go through 500 pages
            page_url = f'https://www.digikala.com/search/?page={page_number}&sort=4'
            await page.goto(page_url)

            # Wait for the page to load
            await page.waitFor(5000)

            # Get the page content
            page_content = await page.content()

            # Parse the page content with BeautifulSoup
            soup = BeautifulSoup(page_content, 'html.parser')

            # Find all product names on the page
            product_cards = soup.find_all('a', class_='d-block pointer pos-relative bg-000 overflow-hidden grow-1 py-3 px-4 px-2-lg h-full-md styles_VerticalProductCard--hover__ud7aD')

            # Extract and write details for each product
            for card in product_cards:

                product_name_element = card.find('h3', class_='styles_VerticalProductCard__productTitle__6zjjN')
                product_name = product_name_element.text.strip()
                
                # Extract product price with error handling
                product_price_element = card.find('div', class_='d-flex ai-center jc-end gap-1 color-700 color-400 text-h5 grow-1')
                if product_price_element:
                    product_price = product_price_element.text.strip()
                    product_price = persian_to_english(product_price)
                else:
                    product_price = None
                
                # Extract product rating with error handling
                product_rating_element = card.find('p', class_='text-body2-strong color-700')
                if product_rating_element:
                    product_rating = product_rating_element.text.strip()
                    product_rating = persian_to_english(product_rating)
                else:
                    product_rating = None
                
                # Extract product link
                product_link = card['href']
                if not product_link.startswith('https://www.digikala.com/'):
                    product_link = 'https://www.digikala.com/' + product_link

                # Extract product id
                product_id = extract_product_id(product_link)

                # Show page number
                page_id = page_number

                # Write the data to the CSV file
                csvwriter.writerow([page_id, product_id, product_name, product_price, product_rating, product_link])
                i += 1
                print(f'Product {i} - ', end='')
            print('')
            print(f'page {page_number} done.')

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
