#Nim4 karimi --[2018-3-16 Fri 22:39]

def echo(anything):
    'echo returns its input argumant'
    return anything

def print_if_true(thing , check):
    '''
    1 . Check wheather the *secend* argument is true.
    2 . If it is , print the *first* argument
    '''
    if check:
        print(thing)

#help(echo)
#help(print_if_true)
