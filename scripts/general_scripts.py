from brownie import network, accounts, config
import eth_utils

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    elif id:
        return accounts.load(id)
    elif not config['networks'][network.show_active()]['local'] is False:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['dev_account_1']['private_key'])

def encode_function_data(initialiser=None, *args):
    if len(args) == 0 or not initialiser:
        return eth_utils.to_bytes(hexstr='0x')
    
    return initialiser.encode_input(*args)

def upgrade(account, proxy, new_implemtation, proxy_admin=None, initialiser=None, *args):
    if proxy_admin:
        if initialiser:
            encoded_function_call = encode_function_data(initialiser, *args)
            tx = proxy_admin.upgradeAndCall(proxy.address, new_implemtation.address, encoded_function_call, {'from':account})
            tx.wait(1)
        else:
            tx = proxy_admin.upgrade(proxy.address, new_implemtation.address, {'from':account})
            tx.wait(1)
    
    elif initialiser:
        encoded_function_call = encode_function_data(initialiser, *args)
        tx = proxy.upgradeToAndCall(new_implemtation.address, encoded_function_call, {'from':account})
        tx.wait(1)

    else:
        tx = proxy.upgradeTo(new_implemtation.address, {'from':account})
        tx.wait(1)

    return tx