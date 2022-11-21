from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'45',
  'limit':'1',
  

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a76db5ff-9af1-4103-8188-ed7b518f1ca4',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  json_string= json.dumps(data['data'])
 
  
  
  print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)