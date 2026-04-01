import requests
import re

# Methods
# GET
# POST
# PUT
# DELETE
# PATCH
# HEAD
# OPTIONS

#### urls no api key
# https://jsonplaceholder.typicode.com <-- fake rest api, provides posts, users, comments, todos
# https://jsonplaceholder.typicode.com/posts/1
# https://httpbin.org <-- lets you inspect requests, headers, status codes
# https://httpbin.org/get
# https://dog.ceo/api/breeds/image/random <-- random dog images
# https://catfact.ninja/fact <-- random cat facts
# https://api.coindesk.com/v1/bpi/currentprice.json <-- crypto price data

### Require free key
# https://api.openweathermap.org/data/2.5/weather <-- OpenWeatherMap, weather data
# params = {"q": "New York", "appid": "YOUR_API_KEY"}
# 
# https://api.nasa.gov
# url = https://api.nasa.gov/planetary/apod <-- space data, images, astronomy picture of the day
# params = {"api_key": "DEMO_KEY"}
# print(requests.get(url, params=params).json())

CAT_URL = 'https://catfact.ninja/fact'
DOG_URL = 'https://dog-api.kinduff.com/api/facts'
CRYPTO_URL = 'https://api.coinbase.com/v2/prices/spot?currency=USD'


def get_info(url):
    response = requests.options(url)

    print(f"Here is the status code: {response.status_code}")
    print(f"Here is the {response.headers.get('Allow')}")
    print(f"{response.text}")

    response_get = requests.get(url)
    print(response_get.json())

def start_program():
    res = input(f"for starters do you want dog cat crypto stuff? type dog cat crypto: ")
    if res == "dog":
        get_info(DOG_URL)
    elif res == "cat":
        get_info(CAT_URL)
    elif res == "crypto":
        get_info(CRYPTO_URL)

start_program()