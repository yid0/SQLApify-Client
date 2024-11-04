from  ..config import BodySettings
from .handler import Handler
from .base_service import BaseService    
    
class UserService(BaseService):
    
    def __init__(self, body: BodySettings, path = "/user"):
        self.path=path
        self.body = body
        super().__init__(self.path)
        
    async def handle_request(self):
        handler = Handler(method="post", url= self.url, path=self.path, body= self.body)       
        return await handler.handle()            