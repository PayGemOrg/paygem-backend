from fastapi import APIRouter
from ..controllers.service_controller import ServiceController
from ..schemas.service import ServiceCreate, ServiceUpdate

router = APIRouter(prefix="/services", tags=["services"])
controller = ServiceController()

@router.post("/")
async def create_service(service: ServiceCreate, user_address: str):
    return await controller.create_service(user_address, service)

@router.get("/{service_id}")
async def get_service(service_id: int):
    return await controller.get_service(service_id)

@router.get("/")
async def get_all_services():
    return await controller.get_all_services()

@router.put("/{service_id}")
async def update_service(service_id: int, service_update: ServiceUpdate, user_address: str):
    return await controller.update_service(user_address, service_id, service_update)

@router.delete("/{service_id}")
async def delete_service(service_id: int, user_address: str):
    return await controller.delete_service(user_address, service_id)
