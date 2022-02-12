from scripts.general_scripts import get_account, encode_function_data, upgrade
from brownie import Box, BoxV2, ProxyAdmin, TransparentUpgradeableProxy, Contract, exceptions
import pytest

def test_proxy_upgardes():
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

    box_v2 = BoxV2.deploy({'from':account})
    proxy_box = Contract.from_abi('BoxV2', proxy.address, BoxV2.abi)

    with pytest.raises(AttributeError):
        proxy_box.increment({'from':account})

    upgrade(account, proxy, box_v2, proxy_admin)

    assert proxy_box.retrieve() == 0

    proxy_box.increment({'from':account}).wait(1)
    
    assert proxy_box.retrieve() == 1

