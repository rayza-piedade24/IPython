import sys
import requests

def main():
    try:
        if sys.argv[1]:
            try:
                coin_price = requests.get(https://api.coindesk.com/v1/bpi/currentprice.json)
                coin_price_usd = coin
            except requests.RequestException:
            sys.exit()
        else:
            sys.exit("Missing command line argument")

    except ValueError:
        sys.exit("Command line is not a number")

main()
