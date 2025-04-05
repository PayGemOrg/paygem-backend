from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract
from fastapi import HTTPException, status
from app.schemas.users import user_metrics_helper
from app.schemas.subscription import subscription_helper
class UserController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def get_user_metrics(self, user_address: str) -> dict:
        try:
            metrics = self.contract.functions.getUserMetrics(user_address).call()
            return {
                "status": "success",
                "data": user_metrics_helper(metrics)
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        
    async def get_next_renewal(self, user_address: str) -> dict:
        try:
            contract_function = self.contract.functions.getUserSubscriptions(user_address)
            subscriptions = contract_function.call()
            # Filter subscriptions that are expired or have a next billing date close to today
            current_time = self.web3.eth.get_block('latest')['timestamp']
            close_renewals = []
            for subscription in subscriptions:
                next_billing_date = subscription[4]
                # 1 week to time
                if next_billing_date <= current_time + 604800:
                    close_renewals.append(subscription_helper(subscription))
            return {
                "status": "success",
                "data": close_renewals
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})