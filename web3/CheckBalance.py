from web3 import Web3 

infura_url = "https://rinkeby.infura.io/v3/c71703b7b9734ff68884062db8d377f0"

web3 = Web3(Web3.HTTPProvider(infura_url))
web3.isConnected()
print(web3.isConnected())
web3.eth.blockNumber
balance = web3.eth.get_balance("0x5A9cBc9821cF17eC0823593b6a2daD9e72a053BC")
print(balance)
web3.fromWei(balance,"ether")
print(web3.fromWei(balance,"ether"))

transaction = web3.eth.get_transaction('0xd93b2f78aa398ef2fc3f004b6f22ff9f00e78fc6c51cd694ab09b0b457318b93')
print(transaction)