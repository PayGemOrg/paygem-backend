from web3 import Web3
from ..helpers.config import settings
from ..helpers.web3_helper import get_contract, handle_transaction

class PlanController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract(self.web3, settings.CONTRACT_ADDRESS, settings.CONTRACT_ABI)

    async def create_plan(self, user_address: str, private_key: str, plan_data: dict) -> dict:
        try:
            contract_function = self.contract.functions.createPlan(
                plan_data.service_id,
                plan_data.merchant_id,
                plan_data.name,
                plan_data.description,
                plan_data.price,
                plan_data.currency,
                plan_data.billing_cycle,
                plan_data.subscribers_limit
            )
            return handle_transaction(self.web3, contract_function, user_address, private_key)
        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def get_plan(self, plan_id: int) -> dict:
        try:
            plan = self.contract.functions.getPlan(plan_id).call()
            return {
                "status": "success",
                "data": {
                    "id": plan[0],
                    "service_id": plan[1],
                    "merchant_id": plan[2],
                    "name": plan[3],
                    "description": plan[4],
                    "price": plan[5],
                    "currency": plan[6],
                    "billing_cycle": plan[7],
                    "is_active": plan[8],
                    "subscribers_limit": plan[9],
                    "subscriber_count": plan[10]
                }
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def toggle_plan_status(self, user_address: str, private_key: str, plan_id: int) -> dict:
        try:
            contract_function = self.contract.functions.togglePlanStatus(plan_id)
            return handle_transaction(self.web3, contract_function, user_address, private_key)
        except Exception as e:
            return {"status": "error", "message": str(e)}
