from fastapi import APIRouter
from app.controllers.users import UserController

router = APIRouter(prefix="/users", tags=["users"])
controller = UserController()

@router.get("/metrics/{user_address}/")
async def get_user_metrics(user_address: str):
    """
    Get user metrics from the smart contract.
    """
    return await controller.get_user_metrics(user_address)

@router.get("/next_renewals/{user_address}/")
async def get_next_renewal(user_address: str):
    """
    Get subscriptions that have expired or their next billing is really close.
    """
    return await controller.get_next_renewal(user_address)