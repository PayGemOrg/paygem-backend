from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.helpers.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.VERSION)


allow_all = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_methods=allow_all,
    allow_headers=allow_all
)

@app.get("/", response_model=dict)
def root():
    return {
        "message": "server is working"
    }