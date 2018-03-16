# Nim4 karimi - --[2018-3-16 Fri 21:27]
# -------------------------------------
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and 
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

print('--'*20)
value = input('Enter number separated by comma , |---> ')
list = value.split(',')
tuple_one = tuple(list)
print('--'*20)
print("list ---> " , list)
print('--'*20)
print("tuple --> " , tuple_one)

