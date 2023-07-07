


from src.controller.testcontroller import Helloworld


class HelloRouter():
    def setRoute(self):
        self.api.add_resource(self.controller,"/Hellow/")
        
    def __init__(self,api):
        self.api=api
        self.controller=Helloworld
        self.setRoute()