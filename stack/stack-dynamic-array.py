class stack_dynamic_array:
    def __init__(self, limit):
        self.data = []
        self.limit = 2 if limit is None else limit

    def is_full(self):
        return len(self.data) == self.limit

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        if self.is_full():
            self.resize()
        self.data.append(value)

    def resize(self):
        self.limit = self.limit * 2

    def pop(self):
        if stack.is_empty():
            print("Underflow exception")
            return
        return self.data.pop()

    def peek(self):
        return self.data[-1]


stack = stack_dynamic_array(None)
stack.push(5)
stack.push(4)
print(stack.limit)
stack.push(3)
stack.push(2)
stack.push(1)
print(stack.limit)

current = stack.pop()
while current is not None:
    print(current)
    current = stack.pop()
