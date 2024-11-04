import asyncio
import sys
import uvloop
import uvicorn
from fastapi import FastAPI
from .service import UserService
from .config import (SQLApifyBodyEnum, BodySettings, AppSettings)
from .service import StatusService

app = FastAPI()

@app.get("/status")
async def status():
    status_service = StatusService()
    return await status_service.handle_request()

    
@app.on_event("startup")
async def startup_event():
    try:
        settings = AppSettings()
        print(f"********* Starting SQLApify Client on {settings.app_env} mode *************") 

        settings = BodySettings(body=SQLApifyBodyEnum.load())      
        user_service = UserService(settings.json())
        return await user_service.handle_request()
    except Exception as e:
        print(f"{e}")


async def main():  
    server = uvicorn.Server()
    await server.serve()
    

if __name__ == "__main__":
    if sys.version_info >= (3, 10):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    else:
        uvloop.install()
        asyncio.run(main())