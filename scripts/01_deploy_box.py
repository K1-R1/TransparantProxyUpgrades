from scripts.general_scripts import get_account
from brownie import Box


def main():
    deploy_box()

def deploy_box():
    account = get_account()
    box = Box.deploy({'from':account})