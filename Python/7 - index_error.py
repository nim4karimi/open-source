#Nim4 Karimi --[2018-3-21 Wed 0:51]
# index_error.py

n = [1, 2, 3, 4, 5]

try:

    n[0] = 10
    n[6] = 60
    
except IndexError as e:
    
    print(e)