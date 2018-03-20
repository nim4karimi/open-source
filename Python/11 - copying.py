# Nim4 karimi --[2018-3-21 Wed 0:56]

# copying.py

import copy

w = ["Python", "Ruby", "Perl"]

c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
c5 = [e for e in w]

c6 = []

for e in w:
    c6.append(e)
    
c7 = []
c7.extend(w)

print(c1, c2, c3, c4, c5, c6, c7)

help(copy)