# Nim4 Karimi - [2018-3-21 Wed]
# traverse3.py

n = [1, 2, 3, 4, 5]

print(list(enumerate(n)))

for e, i in enumerate(n):
    print("n[{0}] = {1}".format(e, i))