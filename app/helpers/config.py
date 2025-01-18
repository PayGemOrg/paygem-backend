from dotenv import load_dotenv
import os
import json

load_dotenv()

class Settings:
    PROJECT_TITLE = os.getenv("PROJECT_TITLE", "Subscription Management API")
    VERSION = os.getenv("VERSION", "1.0.0")
    URI = os.getenv("URI", "")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 20
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "")
    RPC_URL = os.getenv("RPC_URL", "")
    GAS_LIMIT = int(os.getenv("GAS_LIMIT", "200000"))
    GAS_PRICE_GWEI = int(os.getenv("GAS_PRICE_GWEI", "20"))
    CONTRACT_ABI_PATH = "ABI/abi.json"
    
    def __init__(self):
        self.CONTRACT_ABI = self.load_contract_abi()

    def load_contract_abi(self):
        """Load and parse the contract ABI from a file."""
        try:
            with open(self.CONTRACT_ABI_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"ABI file not found at {self.CONTRACT_ABI_PATH}")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON format in the ABI file")
settings = Settings()
