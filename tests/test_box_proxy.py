from scripts.general_scripts import get_account, encode_function_data
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy, Contract


def test_proxy_delegates_calls():
    account = get_account()
    box = Box.deploy({'from':account})
    proxy_admin = ProxyAdmin.deploy({'from': account})
    box_encoded_initialiser_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initialiser_function,
        {'from': account}
    )
    proxy_box = Contract.from_abi('Box', proxy.address, Box.abi)

    assert proxy_box.retrieve() == 0

    proxy_box.store(1, {'from': account}).wait(1)
    
    assert proxy_box.retrieve() == 1
