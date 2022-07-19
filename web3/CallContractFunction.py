import json
from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/c71703b7b9734ff68884062db8d377f0"

web3 = Web3(Web3.HTTPProvider(infura_url))

abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"_description","type":"string"},{"internalType":"address payable","name":"_recipent","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"CreateRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"GetBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Refund","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"contributors","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deadline","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestNo","type":"uint256"}],"name":"makePayment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minimumContribution","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"noOfContributors","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numRequests","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"raisedAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"requests","outputs":[{"internalType":"string","name":"description","type":"string"},{"internalType":"address payable","name":"recipent","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bool","name":"completed","type":"bool"},{"internalType":"uint256","name":"noOfVoter","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sendETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"target","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestNo","type":"uint256"}],"name":"voterRequest","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

address = '0xC3c89eCFe2E6508303799b79696abE411b5C8f5E'

#calling contract through web3
contract = web3.eth.contract(address=address, abi=abi)

print(contract)
getbalance = contract.functions.GetBalance().call()
print(web3.fromWei(getbalance,'ether'))