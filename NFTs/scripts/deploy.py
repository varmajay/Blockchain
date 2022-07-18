from brownie import MyNFT, network, accounts, config


def get_acount():
    if network.show_active() == "Development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_fund_me():
    account = get_acount()
    mynft = MyNFT.deploy({"from":account}, publish_source =True)
    print(f"Contract deployed to {mynft.address}")



def main():
    deploy_fund_me()




#0xfF63b87844D7d6af779928b245dCa57557D0a68a