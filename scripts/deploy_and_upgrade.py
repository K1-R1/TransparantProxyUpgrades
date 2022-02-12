from scripts.general_scripts import get_account, encode_function_data, upgrade
from brownie import Box, BoxV2, ProxyAdmin, TransparentUpgradeableProxy, Contract


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
    proxy_box.store(1, {'from':account}).wait(1)
    print(proxy_box.retrieve())

    box_v2 = BoxV2.deploy({'from':account})
    upgrade(account, proxy, box_v2, proxy_admin)
    proxy_box = Contract.from_abi('BoxV2', proxy.address, BoxV2.abi)
    print('Proxy has been upgraded, new implementation: box_v2')
    proxy_box.increment({'from':account}).wait(1)
    print(proxy_box.retrieve())
