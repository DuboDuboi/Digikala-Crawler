
import requests

response = requests.get(
  url='https://api.scrapingant.com/v2/general?url=https%3A%2F%2Fwww.digikala.com%2F&x-api-key=1d0908f3acf944dfb16d76e6010ef081&proxy_country=SA' 
  ,
)

print('Response Body: ', response.content)