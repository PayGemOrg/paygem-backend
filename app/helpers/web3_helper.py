
from web3 import Web3
from .config import settings
import json

def get_contract(web3: Web3, contract_address: str, contract_abi: str) -> Web3.eth.Contract:
    return web3.eth.contract(address=contract_address, abi=json.loads(contract_abi))

def handle_transaction(web3: Web3, contract_function, user_address: str, private_key: str, value: int = 0):
    try:
        transaction = contract_function.build_transaction({
            'from': user_address,
            'gas': settings.GAS_LIMIT,
            'gasPrice': web3.to_wei(settings.GAS_PRICE_GWEI, 'gwei'),
            'nonce': web3.eth.get_transaction_count(user_address),
            'value': value
        })
        
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        return {
            "status": "success",
            "tx_hash": tx_receipt.transactionHash.hex(),
            "block_number": tx_receipt.blockNumber,
            "gas_used": tx_receipt.gasUsed
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
