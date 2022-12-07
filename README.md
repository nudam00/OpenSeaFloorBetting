# Opensea Floor Betting
Program which allows betting on whether the floor price of a given NFT collection (based on OpenSea) will hold, fall, or rise. The program is based on the Solidity, Python and brownie framework. Tested on Rinkeby.

## Stakeholder.sol
Ethereum smart contract that allows you to send ETH, bet on ETH, send a multiplier and pay out ETH (owner only).

## deploy.py
Allows deploying the contract.

## fund.py
Allows funding the contract.

## helpful_scripts.py
Returns Rinkeby's account.

## scraping.py
It records the floor price before the past time and after the past time. Based on Selenium (it is possible to use the OpenSea API after prior contact).

## stakeholder.py
It brings the whole program together. Allows you to bet by sending ETH, choose the betting option, collection and time.

## brownie-config.yaml
Replace account address.

## .env
Create an .env file and save the account's private key.
export PRIVATE_KEY = ...
