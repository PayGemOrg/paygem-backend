from web3 import Web3
from ..helpers.config import settings
from ..helpers.web3_helper import get_contract, handle_transaction

class SubscriptionController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract(self.web3, settings.CONTRACT_ADDRESS, settings.CONTRACT_ABI)

    async def create_subscription(self, user_address: str, private_key: str, subscription_data: dict) -> dict:
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
                private_key,
                value=subscription_data.amount
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def make_payment(self, user_address: str, private_key: str, subscription_id: int) -> dict:
        try:
            contract_function = self.contract.functions.makePayment(subscription_id)
            return handle_transaction(self.web3, contract_function, user_address, private_key)
        except Exception as e:
            return {"status": "error", "message": str(e)}
        



        