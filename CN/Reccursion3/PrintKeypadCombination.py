def KeypadCombination(n,dictionary,res=""):
    if n == 0:
        print(res)
        return
    lastDigit = n%10
    for val in dictionary[lastDigit]:
        newRes = val + res
        KeypadCombination(n//10,dictionary,newRes)

dictionary = {
        2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",
        7:"pqrs",8:"tuv",9:"wxyz"
}
KeypadCombination(23,dictionary)