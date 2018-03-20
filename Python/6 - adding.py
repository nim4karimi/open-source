#Nim4 Karimi --[2018-3-21 Wed 0:49]

langs = []

langs.append("Python")
langs.append("Perl")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))
print(langs)