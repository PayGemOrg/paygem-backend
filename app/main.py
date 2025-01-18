from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.helpers.config import settings
from app.routers.service_routes import router as service_router
from app.routers.plan_routes import router as plan_router
from app.routers.subscription_routes import router as subscription_router
from app.routers.wallet_routes import router as wallet_router
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.VERSION)


allow_all = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_methods=allow_all,
    allow_headers=allow_all
)


app.include_router(service_router, prefix="/api/v1")
app.include_router(plan_router, prefix="/api/v1")
app.include_router(subscription_router, prefix="/api/v1")
app.include_router(wallet_router, prefix="/api/v1")

@app.get("/", response_model=dict)
def root():
    return {
        "message": "server is working"
    }