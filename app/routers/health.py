from fastapi import APIRouter, FastAPI, status

router = APIRouter(
    tags=["health"]
)

@router.get("/gethealth", status_code=status.HTTP_200_OK,
           summary="Получить статус работы сервиса")
async def get_health():
    return {"status": "healthy"}