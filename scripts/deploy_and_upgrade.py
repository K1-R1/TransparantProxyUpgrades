from scripts.general_scripts import get_account, encode_function_data
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy, Contract


def main():
    deploy_box()

def deploy_box():
    account = get_account()
    box = Box.deploy({'from':account})

    proxy_admin = ProxyAdmin.deploy({'from': account})

    #initialiser = box.store, 1
    box_encoded_initialiser_function = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initialiser_function,
        {'from': account}
    )
    print(f"Proxy deployed to {proxy}, with implemention: Box ...\n")

    proxy_box = Contract.from_abi('Box', proxy.address, Box.abi)

