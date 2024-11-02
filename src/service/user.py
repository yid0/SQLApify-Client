from src.config import BodySettings
from .handler import Handler
from .base_service import BaseService    
    
class UserService(BaseService):
    
    def __init__(self, body: BodySettings, path = "/users"):
        self.path=path
        super().__init__(self.path)
        self.body = body
        
    async def handle_request(self):
        handler = Handler(method="post", url= self.url, path=self.path, body= self.body)       
        print(handler)
        return await handler.handle()      

    
    def __str__(self):
        return str(f"{self.body}")

            