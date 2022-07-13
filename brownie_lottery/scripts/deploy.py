from brownie import accounts,config, Lottery



def deploy_lottery():
    account =accounts[0]
    # print(account)
    # account= accounts.load("jay")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    lotterydeploy = Lottery.deploy({"from":account})
    # print(lotterydeploy)
    stored_value = lotterydeploy.getBalance()
    # print(stored_value)
    transaction = lotterydeploy.store

def main():
    deploy_lottery()