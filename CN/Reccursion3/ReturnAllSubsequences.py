def AllSubSequences(string):
    if len(string) == 0:
        return [""]
    
    smallOutput = AllSubSequences(string[1:])
    lst=[]
    for st in smallOutput:
        lst.append(st)
    for st in smallOutput:
        lst.append(string[0]+st)
    return lst

print(AllSubSequences('abcd'))