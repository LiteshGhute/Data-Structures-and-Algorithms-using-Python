class stack:
    def __init__(self) -> None:
        self.__data = []

    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__data[len(self.__data)-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0

st = stack()
st.push(10)
st.push(20)
st.push(30)
print(st.pop())
print(st.top())
print(st.isEmpty())
print(st.size())