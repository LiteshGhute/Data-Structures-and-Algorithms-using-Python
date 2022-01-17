def LCS(str1,str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0

    #if 1st char of both strings are equal
    if str1[0] == str2[0]:
        op = 1 + LCS(str1[1:],str2[1:])

    #if not equal then
    if str1[0] != str2[0]:
        op = max(LCS(str1[1:],str2),LCS(str1,str2[1:]))

    return op

print(LCS("bedgmc","abdfglc")) 