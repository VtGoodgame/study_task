import uvicorn
from fastapi import FastAPI
from consts import api_version
import routers
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI(title="Study Task API", version=api_version)

app.include_router(routers.files.router)
app.include_router(routers.version.router)
app.include_router(routers.health.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    logger.info(f"API is running on http://localhost:8080 with version {api_version}")