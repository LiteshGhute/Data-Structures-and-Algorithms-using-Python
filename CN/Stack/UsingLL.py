class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class StackLL:
    def __init__(self) -> None:
        self.__head = None
        self.__count = 0

    def push(self,element):
        newNode = Node(element)
        # if self.__head is None:
        #     self.__head = newNode
        #     self.__count += 1
        # else:
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data 

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

st = StackLL()
st.push(10)
st.push(20)
print(st.pop())
print(st.top())
print(st.size())
print(st.isEmpty())
print(st._StackLL__count)