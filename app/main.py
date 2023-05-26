from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .routers import predict

load_dotenv()
START_TIME = str(datetime.now())

# Define Fastapi App
app = FastAPI()
app.include_router(predict.router)


# Default Route
@app.get("/", response_class=JSONResponse)
async def default_gateway(request: Request) -> None:
    return JSONResponse(f"Server running successfully. Last Start Time - {START_TIME}.")
