from brownie import Stakeholder, network, config
from scripts.helpful_scripts import get_account


def deploy_Stakeholder():
    account = get_account()
    stakeholder = Stakeholder.deploy(
        {"from": account, "gas_price": "5 gwei"},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract address: {stakeholder.address}")
    return stakeholder


def main():
    deploy_Stakeholder()
