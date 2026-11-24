class Stack:
    def __init__(self):
        self.data = []

    def push(self, nilai):
        self.data.append(nilai)

    def pop(self):
        # Elemen terakhir dimasukkan menjadi elemen pertama dikeluarkan (LIFO).
        return self.data.pop()


stack = Stack()
stack.push("A")
stack.push("B")
print(stack.pop(), stack.pop())