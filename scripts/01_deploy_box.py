from scripts.general_scripts import get_account, encode_function_data
from brownie import Box, ProxyAdmin


def main():
    deploy_box()

def deploy_box():
    account = get_account()
    box = Box.deploy({'from':account})

    proxy_admin = ProxyAdmin.deploy({'from': account})

    #initialiser = box.store, 1
    box_encoded_initialiser_function = encode_function_data()
    