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
