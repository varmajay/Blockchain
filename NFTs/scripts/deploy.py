from brownie import SimpleCollectible
from scripts.helpful import get_account

sample_token_uri = "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from":account})
    tx = simple_collectible.createCollectible(sample_token_uri,{"from":account})
    tx.wait(1)
    print(f"awesome, you can view your NFTs at {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter() -1 )}")
