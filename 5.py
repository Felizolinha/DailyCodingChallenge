def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def getLeft(a,b):
        return a
    return pair(getLeft)
def cdr(pair):
    def getRight(a,b):
        return b
    return pair(getRight)

par = cons(3,5)
print(car(par))
print(cdr(par))