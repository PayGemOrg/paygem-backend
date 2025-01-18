from fastapi import APIRouter
from ..controllers.plan_controller import PlanController
from ..schemas.plans import PlanCreate

router = APIRouter(prefix="/plans", tags=["plans"])
controller = PlanController()

@router.post("/")
async def create_plan(
    plan: PlanCreate,
    user_address: str,
    private_key: str
):
    return await controller.create_plan(user_address, private_key, plan)

@router.get("/{plan_id}")
async def get_plan(plan_id: int):
    return await controller.get_plan(plan_id)

@router.post("/{plan_id}/toggle")
async def toggle_plan_status(
    plan_id: int,
    user_address: str,
    private_key: str
):
    return await controller.toggle_plan_status(user_address, private_key, plan_id)
