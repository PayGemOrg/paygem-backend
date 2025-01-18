from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract, handle_transaction
from fastapi import HTTPException, status

class WalletController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def make_deposit(self, user_address: str, deposit_amount: float) -> dict:
        try:
            deposit_in_wei = self.web3.to_wei(deposit_amount, 'ether')
            contract_function = self.contract.functions.deposit()
            return handle_transaction(
                self.web3,
                contract_function,
                user_address,
                value=deposit_in_wei
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def get_user_balance(self, user_address: str) -> dict:
        try:
            balance = self.contract.functions.getUserBalance(user_address).call()
            return {
                "status": "success",
                "data": {
                    "balance": self.web3.from_wei(balance, 'ether')
                }
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def withdraw(self, user_address: str, private_key: str, amount: float) -> dict:
        try:
            amount_in_wei = self.web3.to_wei(amount, 'ether')
            contract_function = self.contract.functions.withdraw(amount_in_wei)
            return handle_transaction(self.web3, contract_function, user_address, private_key)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
