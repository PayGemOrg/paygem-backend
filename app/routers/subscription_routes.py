from fastapi import APIRouter
from ..controllers.subscription_controller import SubscriptionController
from ..schemas.subscription import SubscriptionCreate

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])
controller = SubscriptionController()

@router.post("/")
async def create_subscription(
    subscription: SubscriptionCreate,
    user_address: str
):
    return await controller.create_subscription(user_address, subscription)

@router.post("/{subscription_id}/payment")
async def make_payment(
    subscription_id: int,
    user_address: str
):
    return await controller.make_payment(user_address, subscription_id)
