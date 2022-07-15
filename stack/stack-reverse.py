class stack_reverse:
    def __init__(self, limit):
        self.limit = limit
        self.data = []

    def push(self, value):
        if self.is_full():
            print("Overflow")
            return
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow")
            return

        return self.data.pop()

    def reverse(self):
        temp = []
        pop = self.pop()
        while pop is not None:
            temp.append(pop)
            pop = self.pop()
        self.data = temp

    def recursive_reverse(self):
        new_stack = stack_reverse(10)
        return self.recursive_reverse_helper(new_stack)

    def is_full(self):
        return len(self.data) == self.limit

    def is_empty(self):
        return len(self.data) == 0

    def recursive_reverse_helper(self, new_stack):
        if self.is_empty():
            return new_stack
        new_stack.push(self.pop())
        return self.recursive_reverse_helper(new_stack)


stk = stack_reverse(10)
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

stk.reverse()
print(stk.pop())

result = stk.recursive_reverse()
print(result.pop())
