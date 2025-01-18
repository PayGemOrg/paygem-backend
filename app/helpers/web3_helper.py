
from web3 import Web3
from web3.contract import Contract
from app.helpers.config import settings
import json
from fastapi import HTTPException, status

abi_path = "./ABI/abi.json"
abi = None

with open(abi_path, "r") as file:
    abi = json.load(file)


web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))

def get_contract() -> Contract:
    contract = web3.eth.contract(address=settings.CONTRACT_ADDRESS, abi=abi)
    return contract

def handle_transaction(web3: Web3, contract_function, user_address: str, value: int = 0):
    try:
        transaction = contract_function.build_transaction({
            'from': user_address,
            'gas': settings.GAS_LIMIT,
            'gasPrice': web3.to_wei(settings.GAS_PRICE_GWEI, 'gwei'),
            'nonce': web3.eth.get_transaction_count(user_address),
            'value': value
        })
        
        # signed_txn = web3.eth.account.sign_transaction(transaction, settings.PRIVATE_KEY)
        # tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        # return {
        #     "status": "success",
        #     "tx_hash": tx_receipt.transactionHash.hex(),
        #     "block_number": tx_receipt.blockNumber,
        #     "gas_used": tx_receipt.gasUsed
        # }

        return transaction
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
    