import uvicorn
from fastapi import FastAPI
from consts import VERSION, APP_PORT
import routers
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI(title="Study Task API", version=VERSION)

app.include_router(routers.files.router)
app.include_router(routers.version.router)
app.include_router(routers.health.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)
    logger.info(f"API is running on http://localhost:{APP_PORT} with version {VERSION}")
