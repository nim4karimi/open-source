#Nim4 karimi --[2018-3-16 Fri 22:52]

def outer(a,b):
    def inner (c , d):
        return c + d
    return inner(a,b)


print(outer(4,7))