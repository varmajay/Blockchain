from brownie import CrowdFunding, config
from scripts.helpfull import get_account


def deploy_crowdfunding():
    account = get_account()
    crowd_funding = CrowdFunding.deploy(100,3600,{"from":account},publish_source =True)



def main():
    deploy_crowdfunding()