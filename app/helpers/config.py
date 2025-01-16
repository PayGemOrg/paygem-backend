from dotenv import load_dotenv
import os

load_dotenv()

class ENVs:
    URI = os.getenv("URI", "")
    PROJECT_TITLE = os.getenv("PROJECT_TITLE", "")
    VERSION = os.getenv("VERSION")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 20
    CONTRACT_ADDRESS = os.get("CONTRACT_ADDRESS", "")
    RPC_URL = os.get("RPC_URL", "")


settings = ENVs()