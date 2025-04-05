from fastapi import APIRouter
from app.controllers.plan_controller import PlanController
from app.schemas.plans import PlanCreate, PlanUpdate

router = APIRouter(prefix="/plans", tags=["plans"])
controller = PlanController()

@router.post("/")
async def create_plan(plan: PlanCreate, user_address: str):
    return await controller.create_plan(user_address, plan)

@router.get("/{plan_id}")
async def get_plan(plan_id: int):
    return await controller.get_plan(plan_id)

@router.get("/")
async def get_all_plans():
    return await controller.get_all_plans()

@router.put("/{plan_id}")
async def update_plan(plan_id: int, plan_update: PlanUpdate, user_address: str):
    return await controller.update_plan(user_address, plan_id, plan_update)

@router.delete("/{plan_id}")
async def delete_plan(plan_id: int, user_address: str):
    return await controller.delete_plan(user_address, plan_id)

@router.get("/merchant/{user_address}")
async def get_merchant_plans(user_address: str):
    return await controller.get_plans_by_merchant_address(user_address)
