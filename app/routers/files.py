import asyncio
from fastapi import APIRouter  
from scripts import path

router = APIRouter(
    prefix="/files",            
    tags=["files"]
)

@router.get("/getfile", summary="Содержание проекта")
async def get_file():
    file_path = await asyncio.to_thread(path.collect_files_up_to_root)
    if not file_path:
        return {"error": "Files not found"}
    
    return {"file_path": file_path}
