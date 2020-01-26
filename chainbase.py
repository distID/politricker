from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://testnetv3.matic.network"))

from solcx import install_solc, compile_files
install_solc('v0.4.25')
contracts = compile_files(['contracts/politricker.sol'])

# Solidity code deployment
def deploy_contract(contract_interface):
    # Instantiate and deploy contract
    contract = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    # Get transaction hash from deployed contract
    tx_hash = contract.deploy(
        transaction={'from': w3.eth.accounts[1]}
    )
    # Get tx receipt to get contract address
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    return tx_receipt['contractAddress']


contract_address = deploy_contract(contracts.pop("poliTricker"))

