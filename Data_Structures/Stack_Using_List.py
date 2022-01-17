stack=[]
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty!")
    else:
        e=stack.pop()
        print("removed element is:", e)
        print(stack)

while True:
    print("Select the operation: \n1. push \n2. pop \n3. exit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter correct choice")