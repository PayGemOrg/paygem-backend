from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract, handle_transaction
from fastapi import HTTPException, status
from app.schemas.plans import plan_helper, PlanCreate

class PlanController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def create_plan(self, user_address: str, plan_data: PlanCreate) -> dict:
        try:
            # Validate plan price
            if plan_data.price <= 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": "Price must be greater than zero"})
            contract_function = self.contract.functions.createPlan(
                plan_data.service_id,
                plan_data.name,
                plan_data.description,
                plan_data.price,
                plan_data.currency,
                plan_data.billing_cycle,
                plan_data.subscribers_limit
            )
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def get_plan(self, plan_id: int) -> dict:
        try:
            plan = self.contract.functions.getPlan(plan_id).call()
            return {
                "status": "success",
                "data": plan_helper(plan)
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def get_all_plans(self) -> dict:
        """Retrieve all plans using the smart contract's getAllPlans() method"""
        try:
            plans = self.contract.functions.getAllPlans().call()
            return {"status": "success", "data": [
                plan_helper(plan) for plan in plans
            ]}
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def update_plan(self, user_address: str, plan_id: int, update_data: dict) -> dict:
        """Update an existing plan"""
        try:
            contract_function = self.contract.functions.updatePlan(
                plan_id, update_data.name, update_data.price, update_data.billing_cycle
            )
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def delete_plan(self, user_address: str, plan_id: int) -> dict:
        """Delete an existing plan"""
        try:
            contract_function = self.contract.functions.deletePlan(plan_id)
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
        
    async def get_plans_by_merchant_address(self, user_address: str) -> dict:
        """Retrieve all plans by merchant address"""
        try:
            plans = self.contract.functions.getMerchantPlans(user_address).call()
            return {"status": "success", "data": [
                plan_helper(plan) for plan in plans
            ]}
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})
