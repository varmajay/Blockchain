from brownie import accounts
from dotenv import load_dotenv

load_dotenv()

def lottery():
    account = account.load("jay")
    print(account)

def main():
    lottery()