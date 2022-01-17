def KeypadCombination(n,dictionary):
    if n == 0:
        return [""]
    smallOutput = KeypadCombination(n//10,dictionary)
    res = []
    lastDigit = n%10
    for value in dictionary[lastDigit]:
        for st in smallOutput:
            res.append(st+value)
    return res

dictionary = {
        2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",
        7:"pqrs",8:"tuvw",9:"xyz"
}
print(sorted(KeypadCombination(23,dictionary)))