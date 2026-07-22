class Real: 
    def run(self): print('Real')
class Proxy:
    def __init__(self): self.r=Real()
    def run(self): self.r.run()
