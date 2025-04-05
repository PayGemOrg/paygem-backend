from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract, handle_transaction
from fastapi import HTTPException, status
from app.schemas.subscription import subscription_helper

class SubscriptionController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def create_subscription(self, user_address: str, subscription_data: dict) -> dict:
        try:
            contract_function = self.contract.functions.createSubscription(
                subscription_data.plan_id
            )
            contract_function.call()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        
    async def getAllSubsriptionsByUserId(self, user_address: str):
        try:
            contract_function = self.contract.functions.getUserSubscriptions(user_address)
            subscriptions = contract_function.call()
            return {
                "status": "success",
                "data": [
                    subscription_helper(subscription)
                    for subscription in subscriptions
                ]
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        
    async def get_all_subscriptions(self):
        try:
            contract_function = self.contract.functions.getAllSubscriptions()
            subscriptions = contract_function.call()
            return {
                "status": "success",
                "data": [
                    subscription_helper(subscription)
                    for subscription in subscriptions
                ]
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        



        