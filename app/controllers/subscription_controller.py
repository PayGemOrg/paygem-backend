from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract, handle_transaction
from fastapi import HTTPException, status


class SubscriptionController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def create_subscription(self, user_address: str, subscription_data: dict) -> dict:
        try:
            contract_function = self.contract.functions.createSubscription(
                subscription_data.plan_id,
                subscription_data.merchant_id,
                subscription_data.status,
                subscription_data.amount
            )
            return handle_transaction(
                self.web3,
                contract_function,
                user_address,
                value=subscription_data.amount
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def make_payment(self, user_address: str, subscription_id: int) -> dict:
        try:
            contract_function = self.contract.functions.makePayment(subscription_id)
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        



        