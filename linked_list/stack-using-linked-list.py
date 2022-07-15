class node:
    def __init__(self):
        self.value = None
        self.next = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def get_head(self):
        return self.head

    def delete_head(self):
        if self.length == 0:
            return None
        else:
            self.head = self.head.next
        self.length = self.length - 1


class stack:
    def __init__(self):
        self.store = linked_list()

    def push(self, value):
        n1 = node()
        n1.set_value(value)
        self.store.set_head(n1)

    def pop(self):
        popped = self.store.get_head()
        self.store.delete_head()
        return popped

    def traverse(self):
        current = self.pop()
        while current is not None:
            print(current.get_value())
            current = self.pop()


s1 = stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.traverse()
