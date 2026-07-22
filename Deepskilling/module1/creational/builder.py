class House:
    def __init__(self): self.parts=[]
class Builder:
    def build(self):
        h=House(); h.parts=['Walls','Roof']; return h
