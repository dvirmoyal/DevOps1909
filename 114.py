from http.client import responses

import requests

responses = requests.get("https://he.wikipedia.org/wiki/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99")
  if responses.status_code == 200:
   print("wikipedia page found")