#Nim4 karimi --[2018-3-21 Wed 0:53]

# removing.py

langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

lang = langs.pop(3)
print("{0} was removed".format(lang))

lang = langs.pop()
print("{0} was removed".format(lang))

print(langs)

langs.remove("Ruby")
print(langs)