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

    def insert_in_order(self, node):
        if self.length == 0:
            self.set_head(node)
        else:
            current = self.head
            prev = None
            while current is not None and current.get_value() > node.get_value():
                prev = current
                current = current.get_next()
            if prev is None:
                self.set_head(node)
            else:
                node.set_next(current)
                prev.set_next(node)
            self.length = self.length + 1

    def remove_duplicates(self):
        current = self.head
        while current and current.get_next():
            next = current.get_next()
            if current.get_value() == next.get_value():
                current.set_next(next.get_next())
            current = current.get_next()

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()


n1 = node()
n1.set_value(1)

n2 = node()
n2.set_value(2)

n3 = node()
n3.set_value(3)

n4 = node()
n4.set_value(4)

n = node()
n.set_value(2)

ll = linked_list()
ll.insert_in_order(n1)
ll.insert_in_order(n4)
ll.insert_in_order(n3)
ll.insert_in_order(n2)
ll.insert_in_order(n)

ll.traverse()
ll.remove_duplicates()
ll.traverse()
