class Dog: pass
class Cat: pass
class Factory:
    def create(self,t): return Dog() if t=='dog' else Cat()
