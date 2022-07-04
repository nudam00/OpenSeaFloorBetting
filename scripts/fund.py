from brownie import Stakeholder
from scripts.helpful_scripts import get_account


def fund():
    stakeholder = Stakeholder[-1]
    account = get_account()
    print("How much ETH do you want to fund?")
    eth = float(input())
    eth = eth * 10**18
    print("Sending ETH...")
    stakeholder.fund({"from": account, "value": eth, "gas_price": "5 gwei"})


def main():
    fund()
