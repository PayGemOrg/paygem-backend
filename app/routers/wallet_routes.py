
from fastapi import APIRouter
from ..controllers.wallet_controllers import WalletController

router = APIRouter(prefix="/wallet", tags=["wallet"])
controller = WalletController()

@router.post("/deposit")
async def deposit(
    amount: float,
    user_address: str
):
    return await controller.make_deposit(user_address, amount)

@router.get("/balance/{user_address}")
async def get_user_balance(user_address: str):
    return await controller.get_user_balance(user_address)

@router.post("/withdraw")
async def withdraw(
    amount: float,
    user_address: str
):
    return await controller.withdraw(user_address, amount)