
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
contract = web3.eth.contract(address=address, abi=abi)



sender_address = "0x5A9cBc9821cF17eC0823593b6a2daD9e72a053BC"

balance = web3.eth.get_balance(sender_address)
eth_bal = web3.fromWei(balance, 'ether')
print('My Test Eth Balance is: ', eth_bal)

tokenToBuy = web3.toChecksumAddress("0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984")   #Uni Token Address
spend = web3.toChecksumAddress("0xc778417E063141139Fce010982780140Aa0cD5Ab")  # wbnb contract # weth Token address

nonce = web3.eth.get_transaction_count(sender_address)

uniswapv2_txn = contract.functions.swapExactETHForTokens(
    10000000000,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [spend, tokenToBuy],
    sender_address,
    (int(time.time()) + 100000)
).buildTransaction({
    'from': sender_address,
    'value': web3.toWei(0.1, 'ether'),  
    'gas': 2000000,
    'nonce': nonce,
})

signed_txn = web3.eth.account.sign_transaction(uniswapv2_txn, private_key=os.getenv("PRIVATE_KEY"))
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(web3.toHex(tx_token))

