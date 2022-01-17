def Permuatation(string):
    if len(string) == 0:
        return [""]
    res = []
    for i in range(len(string)):
        smallOutput = Permuatation(string[:i]+string[i+1:])
        for sub in smallOutput:
            res.append(string[i]+sub)
    return res
print(Permuatation("abc"))