# contract_address = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D

from web3 import Web3
import json
from dotenv import load_dotenv
import time
import os
from web3.middleware import geth_poa_middleware


load_dotenv()

infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(web3.isConnected())

# uniswap address and abi
abi = json.load(open('abi.json'))
address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
contract = web3.eth.contract(address=address, abi=abi) #connecting to Contract 

# tokenValue = web3.toWei(input("Enter amount you want to sell: "), 'ether')
# int(tokenValue)

#Account Addresss 
sender_address = "0x5A9cBc9821cF17eC0823593b6a2daD9e72a053BC"

#Account Eth balance
balance = web3.eth.get_balance(sender_address)
eth_bal = web3.fromWei(balance, 'ether')
print('My Test Eth Balance is: ', eth_bal)

#Account Uni Balance
uniswap_address = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"
uniswap_abi = json.load(open("uniswap-abi.json"))
token = web3.eth.contract(address=uniswap_address, abi=uniswap_abi)
uni_balance = token.functions.balanceOf(sender_address).call() 
token_balance = web3.fromWei(uni_balance, 'ether')
print('My Test Uni Balance is: ',token_balance)

tokenToBuy = web3.toChecksumAddress("0x3B00Ef435fA4FcFF5C209a37d1f3dcff37c705aD") # USDT token Address
spend = web3.toChecksumAddress("0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984")  # UNI token Address

nonce = web3.eth.get_transaction_count(sender_address)



#calling Uniswap Contract
uniswapv2_txn = contract.functions.swapExactTokensForTokens(
    100000000000000000000,
    1000000000000,
    [spend,tokenToBuy],
    sender_address,
    (int(time.time()) + 1000000),
).buildTransaction({
  'from': sender_address,
#   'value': web3.toWei(0,'ether'),
  'gas': 200000,
  'gasPrice': web3.toWei('10','gwei'),
  'nonce': nonce,
})
# print(uniswapv2_txn)
signed_txn = web3.eth.account.sign_transaction(uniswapv2_txn, private_key=os.getenv("PRIVATE_KEY"))
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(web3.toHex(tx_token))

