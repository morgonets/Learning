import json 
import requests

FILENAME = "data.json" 
URL_Link = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

#!function to print the rates
def print_rates(data):
    print("\tCurrency Base Currency\t | Buy / Sale")
    print("\t---------------------------------------------")
    for cur in data:
        print(f"\t{cur['ccy']}\t {cur['base_ccy']}\t\t | {cur['buy']}/{cur['sale']}")
#!Trying to fetch data from API 
try:
    print("Fetching from API...")
    response = requests.get(URL_Link, timeout=5)
    response.raise_for_status()

    data = response.json()
    print_rates(data)

    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
#!If it fails, load from cache
except requests.exceptions.RequestException:
    print("No internet connection, loading cache...")

    try:
        with open(FILENAME, "r") as f:
            dataset = json.load(f)

        print_rates(dataset)
#!If cache is also unavailable, print error
    except FileNotFoundError:
        print("No cache available")