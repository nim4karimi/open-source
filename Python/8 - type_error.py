#Nim4 karimi --[2018-3-21 Wed 0:52]

# type_error.py

n = [1, 2, 3, 4, 5]

try:
    print(n[1])
    print(n['2'])
    
except TypeError as e:
    
    print("Error in file {0}".format( __file__))
    print("Message: {0}".format(e))