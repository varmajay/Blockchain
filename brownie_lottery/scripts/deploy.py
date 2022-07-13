from brownie import accounts,config, Lottery, network

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_lottery():
    account =get_account()
    # print(account)
    # account= accounts.load("jay")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    lotterydeploy = Lottery.deploy({"from":account})
    # # print(lotterydeploy)
    # stored_value = lotterydeploy.getBalance()
    # # print(stored_value)
    # transaction = lotterydeploy.store

def main():
    deploy_lottery()