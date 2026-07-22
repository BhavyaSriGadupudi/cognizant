class Old:
    def old(self): return 'old'
class Adapter:
    def __init__(self,o): self.o=o
    def new(self): return self.o.old()
