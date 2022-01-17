def convert(string):
    if len(string) == 0:
        return string
    smallOutput = convert(string[1:])
    if string[0] == 'a':
        return 'b' + smallOutput
    else:
        return string[0] + smallOutput
print(convert('aakjhjbaakjhkjaa'))