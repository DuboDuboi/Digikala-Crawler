import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    browser = await launch({"headless": True})
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')

    await page.goto('https://www.digikala.com/search/?page=1')

    # Wait for the page to load
    await page.waitFor(5000)

    # Get the page content
    page_content = await page.content()

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all product names on the page
    product_name_elements = soup.find_all('h3', class_='styles_VerticalProductCard__productTitle__6zjjN')

    # Extract and print all product names
    for element in product_name_elements:
        product_name = element.text.strip()
        print('Product Name:', product_name)

    await page.screenshot({'path': 'screenshot.png'})

    ## Next Steps

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
