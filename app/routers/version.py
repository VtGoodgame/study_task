from fastapi import APIRouter, status
from consts import api_version

router = APIRouter(
    prefix="/versions",            
    tags=["versions"]
)

@router.get("/getversion", status_code=status.HTTP_200_OK,
           summary="Получить актуальную версию API")
async def get_version():
    return {"version": api_version,
            "version_info": "Version details"}