# Nim4 Karimi --[2018-3-16 Fri 22:55]

def knights(saying):
    def inner(qoute):
        return "We are the Knights who say : %s" %qoute
    return inner(saying)


print(knights("Nim4 is really cool B-)"))