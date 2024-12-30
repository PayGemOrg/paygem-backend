from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_model=dict)
def root():
    return {
        "message": "server is working"
    }