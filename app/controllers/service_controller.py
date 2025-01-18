
from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract, handle_transaction
from fastapi import HTTPException, status
from app.schemas.service import ServiceCreate

class ServiceController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()

    async def create_service(self, user_address: str, service_data: ServiceCreate) -> dict:
        try:
            contract_function = self.contract.functions.createService(
                service_data.name,
                service_data.description,
                service_data.tags
            )
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def get_service(self, service_id: int) -> dict:
        try:
            service = self.contract.functions.getService(service_id).call()
            return {
                "status": "success",
                "data": {
                    "id": service[0],
                    "merchant": service[1],
                    "name": service[2],
                    "description": service[3],
                    "is_active": service[4],
                    "tags": service[5]
                }
            }
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})

    async def toggle_service_status(self, user_address: str, service_id: int) -> dict:
        try:
            contract_function = self.contract.functions.toggleServiceStatus(service_id)
            return handle_transaction(self.web3, contract_function, user_address)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": str(e)})