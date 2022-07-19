import eth_utils
from brownie import accounts,network,config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]


def get_account(number=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if number:
        return accounts[number]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None

def encode_function_data(initializer=None, *args):
    if len(args)==0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
        

    return initializer.encode_input(*args)


def upgrade(account,proxy,newimplementation_address,proxy_admin_contract=None,initializer=None,*args):
    if proxy_admin_contract:
        if initializer:
            encoded_function_call = encode_function_data(initializer, *args)
            transaction = proxy_admin_contract.upgradeAndCall(
                proxy.address,
                newimplementation_address,
                encoded_function_call,
                {"from": account},
            )
        else:
            transaction = proxy_admin_contract.upgrade(
                proxy.address, newimplementation_address, {"from": account}
            )
    else:
        if initializer:
                encoded_function_call = encode_function_data(initializer, *args)
                transaction = proxy.upgradeToAndCall(
                newimplementation_address, encoded_function_call, {"from": account}
            )
        else:
            transaction = proxy.upgradeTo(newimplementation_address, {"from": account})
    return transaction      