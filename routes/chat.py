from fastapi import APIRouter

from services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

service = ChatService()


@router.get("/")
def chat():

    return service.chat()
