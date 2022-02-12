# TransparantProxyUpgrades

<br/>
<p align="center">
<a href="https://blog.openzeppelin.com/proxy-patterns/" target="_blank">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/upgrades-mix/main/img/proxy-pattern.png" width="400" alt="OpenZeppelin Proxy logo">
</a>
</p>
<br/>

This repo uses the Transparent Proxy pattern for upgrading smart contracts. It uses most of the code from openzeppelin's repo, and adds brownie scripts on top. 
This repo contains deployment scripts that will:
1. Deploy a `Box` implementation contract
2. Deploy a `ProxyAdmin` contract to be the admin of the proxy
3. Deploy a `TransparentUpgradeableProxy` to be the proxy for the implementations
   
Then, the upgrade script will:

4. Deploy a new Box implementation `BoxV2`
5. Upgrade the proxy to point to the new implementation contract. 
6. Then it will call a function only `BoxV2` can call

The contract is designed to be deployed to:
- Rinkeby test network

The contract has been unit tested locally, with intergration testing performed on Rinkeby.

## Made with
- solidity
- python
- brownie

### This repo is a project created during the course;
- smartcontractkit/full-blockchain-solidity-course-py
