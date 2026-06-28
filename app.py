from fastapi import FastAPI

from routes.chat import router as chat_router
from routes.health import router as health_router

app = FastAPI(
    title="AI-Chat",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"AI-Chat",

        "status":"running"

    }
