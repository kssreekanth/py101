class stack_in_array:
    def __init__(self, limit):
        self.limit = limit
        self.array = [None] * limit
        self.top1 = -1
        self.top2 = self.limit

    def push_stack1(self, value):
        self.top1 = self.top1 + 1
        self.array[self.top1] = value

    def push_stack2(self, value):
        self.top2 = self.top2 - 1
        self.array[self.top2] = value

    def pop_stack1(self):
        result = self.array[self.top1]
        self.top1 = self.top1 - 1
        return result

    def pop_stack2(self):
        result = self.array[self.top2]
        self.top2 = self.top2 + 1
        return result

    def is_stack1_full(self):
        return self.top1 >= self.top2 - 1

    def is_stack1_empty(self):
        return self.top1 == -1

    def is_stack2_full(self):
        return self.top2 <= self.top1 + 1

    def is_stack2_empty(self):
        return self.top2 == self.limit


stack_array = stack_in_array(10)
stack_array.push_stack1(1)
stack_array.push_stack1(2)
stack_array.push_stack1(3)
stack_array.push_stack1(4)
stack_array.push_stack1(5)

stack_array.push_stack2(1)
stack_array.push_stack2(2)
stack_array.push_stack2(3)
stack_array.push_stack2(4)
stack_array.push_stack2(5)

print(stack_array.top1)
print(stack_array.top2)

print(stack_array.pop_stack1())
print(stack_array.pop_stack2())

print(stack_array.pop_stack1())
print(stack_array.pop_stack2())

print(stack_array.pop_stack1())
print(stack_array.pop_stack2())

print(stack_array.pop_stack1())
print(stack_array.pop_stack2())
