from brownie import FundMe, network, accounts, config


def get_acount():
    if network.show_active() == "Development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_fund_me():
    account = get_acount()
    fundme = FundMe.deploy({"from":account}, publish_source =True)
    print(f"Contract deployed to {fundme.address}")



def main():
    deploy_fund_me()