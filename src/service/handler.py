import httpx
from fastapi import Request, Response

class Handler:
    
    def __init__(self, method, url: str = None, path: str = "", body = None):
        self.method = method
        self.url = url
        self.path= path
        self.body = body
        
    async def handle(self):
        async with httpx.AsyncClient() as client:
            from os import getenv
            headers = {
                "caller": str(getenv("APP_SECRET", "app_secret"))
            }
            req: Request = client.build_request(method=self.method, url=(self.url + self.path), headers=headers, json=self.body) 
            response: Response = await client.send(request=req, stream=False)
        return response.json()