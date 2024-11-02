import asyncio
import sys
import uvloop
import uvicorn
from fastapi import FastAPI
from .service import UserService
from .config import SQLApifyBodyEnum
from .service import StatusService

app = FastAPI()

@app.get("/status")
async def status():
    status_service = StatusService()
    print(status_service)
    return await status_service.handle_request()

async def main():
    from os import getenv
    app_env = getenv("SQLAPIFY_CLIENT_ENV", "dev")
    print(f"********* Starting SQLApify Client , APP_ENV: {app_env} *************") 

    server = uvicorn.Server()
    await server.serve()
    

if __name__ == "__main__":
    if sys.version_info >= (3, 8):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    else:
        uvloop.install()
        asyncio.run(main())


    
@app.on_event("startup")
async def startup_event():
    try:
        print("*********** STARTUP SERVICE **************")
        user_service = UserService(body=SQLApifyBodyEnum.load())
        await user_service.handle_request()
    except Exception as e:
        print(f"{e}")