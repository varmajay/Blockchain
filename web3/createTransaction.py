from web3 import Web3 
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())


account1 = "0x5293c9dBC0dC54ED7B727BE1d7b2b2ddFbc5cAE9"
account2 = "0xCc0b869afB16a38B44a833055e51945e52Cf94A5"

private_key = "b4a99edaf9e1485e1bf404012decbeb17c1a694a6ab98065eea474d738a5853f"


nonce = web3.eth.getTransactionCount(account1)
# print(nonce)
tx = {
    "nonce":nonce,
    "to":account2,
    "value":web3.toWei(1,'ether'),
    "gas":2000000,
    "gasPrice":web3.toWei(50,"gwei"),
}



tx_signed = web3.eth.account.sign_transaction(tx,private_key)
tx_hash = web3.eth.send_raw_transaction(tx_signed.rawTransaction)
print(web3.toHex(tx_hash))
