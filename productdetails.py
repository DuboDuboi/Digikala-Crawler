
import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'cd6b7fda-abcc-47ae-89f8-0596b8668aed',
      'url': 'https://www.digikala.com/', 
      'country': 'us', 
  },
)

print('Response Body: ', response.content)