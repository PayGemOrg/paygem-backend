from web3 import Web3
from app.helpers.config import settings
import json

w3 = Web3(Web3.HTTPProvider(settings.RPC_URL))
abi_path = "./ABI/abi.json"
abi = None

with open(abi_path, "r") as file:
    abi = json.load(file)
    print(abi)

CONTRACT = w3.eth.contract(address=settings.CONTRACT_ADDRESS, abi=abi)
