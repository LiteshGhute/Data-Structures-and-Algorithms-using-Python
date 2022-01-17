def replacePi(string):
    l = len(string)
    if l == 0 or l ==1:
        return string
    
    if string[0] == 'p' and string[1] == 'i':
        smallOutput = replacePi(string[2:])
        return '3.14' + smallOutput
    else:
        smallOutput = replacePi(string[1:])
        return string[0]+smallOutput

print(replacePi('vjhpihbj'))