class node:
    def __init__(self):
        self.value = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def delete_head(self):
        self.head = self.head.get_next()
        self.length = self.length - 1

    def is_empty(self):
        return self.length == 0


class stack_using_linked_list:
    def __init__(self):
        self.data = linked_list()

    def push(self, value):
        new_node = node()
        new_node.set_value(value)
        self.data.set_head(new_node)

    def pop(self):
        if self.data.is_empty():
            print("Underflow exception")
            return
        result = self.data.head
        self.data.delete_head()
        return result

    def peek(self):
        return self.data.head


stack = stack_using_linked_list()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

current = stack.pop()
while current is not None:
    print(current.get_value())
    current = stack.pop()
