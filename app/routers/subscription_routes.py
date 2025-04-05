from fastapi import APIRouter
from app.controllers.subscription_controller import SubscriptionController
from app.schemas.subscription import SubscriptionCreate

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])
controller = SubscriptionController()

@router.post("/", response_model=dict)
async def create_subscription(
    subscription: SubscriptionCreate,
    user_address: str
):
    return await controller.create_subscription(user_address, subscription)

@router.get("/{user_address}/")
async def get_subscriptions_by_user_address(
    user_address: str
):
    return await controller.getAllSubsriptionsByUserId(user_address)

@router.get("/")
async def get_all_subscriptions():
    return await controller.get_all_subscriptions()