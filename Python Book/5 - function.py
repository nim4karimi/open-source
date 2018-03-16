#Nim4 karimi --[2018-3-16 Fri 22:49]

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func , *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1,2,3,4)) # return 10