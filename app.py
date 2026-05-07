from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI running on Lambda with Docker!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

handler = Mangum(app)