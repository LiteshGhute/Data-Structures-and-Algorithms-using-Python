def PrintSubSequences(string,res=""):
    #base case
    if len(string) == 0:
        print(res)
        return
    #don't include 0th char
    PrintSubSequences(string[1:],res)
    #include 0th char
    newRes = res + string[0]
    PrintSubSequences(string[1:],newRes)
PrintSubSequences('abc')