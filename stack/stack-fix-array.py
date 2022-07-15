# pythons [] are list only, it can expand as much we want.
class stack_fix_array:
    def __init__(self, limit):
        self.data = []
        self.limit = limit

    def is_full(self):
        return len(self.data) == self.limit

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        if self.is_full():
            print("overflow exception")
            return
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow exception")
            return
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            print("Underflow exception")
            return
        return self.data[-1]


stack = stack_fix_array(10)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

print("peek", stack.peek())

current = stack.pop()
while current is not None:
    print(current)
    current = stack.pop()

current = stack.pop()
