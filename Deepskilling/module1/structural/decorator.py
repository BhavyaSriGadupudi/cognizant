def star(f):
    def w(): print('*');f();print('*')
    return w
