from solcx import compile_standard, install_solc
import json
from web3 import Web3
import web3
import os
from dotenv import load_dotenv 

load_dotenv()

install_solc("0.8.0")



with open("./lottery.sol","r") as file:
    lottery = file.read() 

#complie our Solidity:

compiled_sol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"lottery.sol":{"content":lottery}},
        "settings":{
            "outputSelection":{
                "*":{
                    "*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)


with open("compiled_code.json","w") as file:
    json.dump(compiled_sol,file)



#get Bytecode

bytecode = compiled_sol["contracts"]["lottery.sol"]["Lottery"]["evm"]["bytecode"]["object"]
# print(bytecode)

#Get abi 
abi = compiled_sol["contracts"]["lottery.sol"]["Lottery"]["abi"]
# print(abi)


#for Connecting to ganache 

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xaeB67958Ec51aA0603F1be4018aEF84Aa1232F77"
private_key = os.getenv("PRIVATE_KEY")
# print(private_key)


#create the contract in python 
Lottery = w3.eth.contract(abi=abi,bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)
# print(nounce)


transaction = Lottery.constructor().build_transaction(
    {"chainId":chain_id,"from":my_address,"nonce":nonce ,"gasPrice": w3.eth.gas_price}
    )
# print(transaction)
signed_txn = w3.eth.account.sign_transaction(transaction,private_key = private_key)

#Send this signed transaction 
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt =w3.eth.wait_for_transaction_receipt(tx_hash)


lottery = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
# print(lottery.functions.getBalance().call())