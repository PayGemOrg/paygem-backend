from app.helpers.database import connect_database

db = connect_database()

collections = {
    "users": db["users"],
}