from eth_utils import to_hex
from web3 import Web3 

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account1 = "0xc2D4106dEa4930F610b6173a1B1cBC36E34Bb950"
account2 = "0x613ace493ef3308EcAa6eA9Ed9E3242678563dE0"

private_key = "c30f10eb16100561bd5ac8a73e3046bf384050cd27d97581f8bfc3694e7b1737"

nonce = web3.eth.getTransactionCount(account1)

tx = {
    'nonce':nonce,
    'to':account2,
    'value':web3.toWei(1,'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei(50,'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx,private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(to_hex(tx_hash))