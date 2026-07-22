class Model: data='Hello'
class View:
    def show(self,d): print(d)
class Controller:
    def __init__(self): self.m=Model(); self.v=View()
    def update(self): self.v.show(self.m.data)
