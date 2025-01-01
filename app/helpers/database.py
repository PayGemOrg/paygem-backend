from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
import certifi
from app.helpers.config import settings

def connect_database():
    client = MongoClient(settings.URI, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    try:
        client.admin.command('ping')
        db = client['paygem']
        return db
    except Exception as e:
        print(e)