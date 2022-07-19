from .helpfull import*
from brownie import Box,ProxyAdmin,TransparentUpgradeableProxy,Contract,BoxV2

def main():
    account=get_account()
    box=Box.deploy({'from':account},publish_source =True)
    
    proxy_admin=ProxyAdmin.deploy({'from':account},publish_source =True)
    
    box_encoded_initializer_function = encode_function_data()
    
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
        publish_source =True,
    )
    print(f"Proxy deployed to {proxy} ! You can now upgrade it to BoxV2!")
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    proxy_box.store(1,{'from':account})
    # proxy_box.({'from':account})
  
    box2=BoxV2.deploy({'from':account}, publish_source =True)
    
    upgrade_transaction=upgrade(account, proxy, box2, proxy_admin_contract=proxy_admin)   
    upgrade_transaction.wait(1)
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    proxy_box.increment({"from": account})
    print(proxy_box.retrieve())