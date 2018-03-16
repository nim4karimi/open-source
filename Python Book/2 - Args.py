# Nim4 karimi - --[2018-3-16 Fri 22:35]

def print_more(required1, required2, *args):
    print('Need this one :' , required1)
    print('Need this one too : ', required2)
    print('All the rest :', args)


print_more('cap','gloves','scarf', 'monobox','mustache wax')