from .base_service import BaseService
from .handler import Handler

class StatusService(BaseService):
    
    def __init__(self, path = "/status"):
        self.path=path
        super().__init__(self.path)
    
    async def handle_request(self):      
        handler = Handler(method="get", url= self.url, path=self.path)       
        return await handler.handle()