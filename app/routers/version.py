from fastapi import APIRouter, status
from consts import VERSION

router = APIRouter( 
    tags=["versions"]
)

@router.get("/getversion", status_code=status.HTTP_200_OK,
           summary="Получить актуальную версию API")
async def get_version():
    return {"version": VERSION,
            "version_info": "Version details"}