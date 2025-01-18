from fastapi import APIRouter
from ..controllers.service_controller import ServiceController
from ..schemas.service import ServiceCreate

router = APIRouter(prefix="/services", tags=["services"])
controller = ServiceController()

@router.post("/")
async def create_service(
    service: ServiceCreate,
    user_address: str,
    private_key: str
):
    return await controller.create_service(user_address, private_key, service)

@router.get("/{service_id}")
async def get_service(service_id: int):
    return await controller.get_service(service_id)

@router.post("/{service_id}/toggle")
async def toggle_service_status(
    service_id: int,
    user_address: str,
    private_key: str
):
    return await controller.toggle_service_status(user_address, private_key, service_id)
