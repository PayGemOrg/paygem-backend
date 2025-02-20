from web3 import Web3
from app.helpers.config import settings
from app.helpers.web3_helper import get_contract 

class GetterController:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
        self.contract = get_contract()