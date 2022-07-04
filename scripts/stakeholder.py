from brownie import Stakeholder
from scripts.helpful_scripts import get_account
from random import randrange
from scripts.scraping import Scraping

account = get_account()


def bet():
    stakeholder = Stakeholder[-1]
    print("How much ETH are you betting on?")
    eth = float(input())
    eth = eth * 10**18
    print("Sending ETH...")
    stakeholder.bet({"from": account, "value": eth, "gas_price": "5 gwei"})
    print(
        "Enter 1 if you are betting on a decrease\n"
        "Enter 2 if you are betting on a rise\n"
        "Enter 3 if you're betting on maintenance"
    )
    _betNumber = input()
    multi = randrange(2, 4, 1)
    stakeholder.storeMulti(multi, {"from": account, "gas_price": "5 gwei"})
    return float(_betNumber)


def withdraw(account):
    stakeholder = Stakeholder[-1]
    stakeholder.withdraw(account, {"from": account, "gas_price": "5 gwei"})


def retrieveMulti(_account):
    stakeholder = Stakeholder[-1]
    return stakeholder.retrieveMulti(_account)


def retrieveAmount(_account):
    stakeholder = Stakeholder[-1]
    return stakeholder.retrieveAmount(_account)*retrieveMulti(_account)


def scrapFloorPrice():
    print("Enter the url of the collection you are betting on")
    url = input()
    print(
        "Within what time do you think the price of the collection will change (give time in minutes)"
    )
    cooldown = float(input())
    scraper = Scraping(url, cooldown)
    floor_price1, floor_price2 = scraper.process()
    return [floor_price1, floor_price2]


def main():
    while exit:
        input(exit)
        betNumber = bet()
        multi = retrieveMulti(account)
        floor_price1, floor_price2 = scrapFloorPrice()
        won = retrieveAmount(account)
        print("The multiplier is {}".format(multi))
        if betNumber == 1 and floor_price2 < floor_price1:
            print("You hit! You won {}".format(won))
            withdraw(account)
        elif betNumber == 2 and floor_price2 > floor_price1:
            print("You hit! You won {}".format(won))
            withdraw(account)
        elif betNumber == 3 and floor_price2 == floor_price1:
            print("You hit! You won {}".format(won))
            withdraw(account)
        else:
            print("Unfortunately you missed")
