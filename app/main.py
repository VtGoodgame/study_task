from fastapi import FastAPI
import uvicorn

import routers
from consts import api_version

app = FastAPI(title="Study Task API", version=api_version)

app.include_router(routers.files.router)
app.include_router(routers.version.router)
app.include_router(routers.health.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)