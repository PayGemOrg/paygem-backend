from web3 import Web3
from app.helpers.config import settings


def make_deposit(user_address: str, private_key: str, deposit_amount: float) -> dict:
    try:
        # Initialize Web3 and Contract
        web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        contract = get_contract(web3, settings.CONTRACT_ADDRESS, settings.CONTRACT_ABI)

        # Convert deposit amount to Wei (Ethereum uses Wei for transactions)
        deposit_in_wei = web3.toWei(deposit_amount, 'ether')

        # Build the transaction
        txn = contract.functions.deposit().buildTransaction({
            'from': user_address,
            'value': deposit_in_wei,
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': web3.eth.getTransactionCount(user_address),
        })

        # Sign the transaction with the user's private key
        signed_txn = web3.eth.account.signTransaction(txn, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        return {
            "status": "success",
            "tx_hash": tx_receipt.transactionHash.hex(),
            "block_number": tx_receipt.blockNumber,
            "gas_used": tx_receipt.gasUsed,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }