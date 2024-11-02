from abc import ABC

class BaseService(ABC):
    path: str = ""
    url: str
    def __init__(self, path):
        from os import getenv
        print(getenv("SQLAPIFY_ENDPOINT"))
        self.url = str(getenv("SQLAPIFY_ENDPOINT"))
        self.path = path
        
    @classmethod
    def handle_request(self):
        pass