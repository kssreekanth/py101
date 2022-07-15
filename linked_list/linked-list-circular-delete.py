class ccnode:
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


class cyclic_linked_list_v1:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, node):
        if self.length == 0:
            self.head = node
            node.set_next(self.head)
        else:
            current = self.head
            while current is not None and current.get_next().get_value() != self.head.get_value():
                current = current.get_next()
            node.set_next(self.head)
            self.head = node
            current.set_next(self.head)
        self.length = self.length + 1

    def delete_head(self):
        if self.length == 0:
            return
        current = self.head
        while current is not None and current.get_next().get_value() != self.head.get_value():
            current = current.get_next()
        self.head = self.head.get_next()
        current.set_next(self.head)
        self.length = self.length - 1

    def delete_tail(self):
        if self.length == 0:
            return
        current = self.head
        while current is not None and current.get_next().get_value() != self.head.get_value() \
                and current.get_next().get_next().get_value() != self.head.get_value():
            current = current.get_next()
        current.set_next(self.head)
        self.length = self.length - 1

    def delete_at_position(self, pos):
        if pos > self.length - 1 or pos < 0:
            return

        if pos == 0:
            self.delete_head()
        elif pos == self.length - 1:
            self.delete_tail()
        else:
            index = 0
            current = self.head
            while current is not None and current.get_next().get_value() != self.head.get_value() and pos != index + 1:
                current = current.get_next()
                index = index + 1

            deleted = current.get_next()
            current.set_next(deleted.get_next())

    def traverse(self):
        current = self.head
        print(current.get_value())
        while current is not None and current.get_next().get_value() != self.head.get_value():
            current = current.get_next()
            print(current.get_value())


ddl = cyclic_linked_list_v1()
node1 = ccnode()
node1.set_value(1)
ddl.insert_at_beginning(node1)

node2 = ccnode()
node2.set_value(2)
ddl.insert_at_beginning(node2)

node3 = ccnode()
node3.set_value(3)
ddl.insert_at_beginning(node3)

node4 = ccnode()
node4.set_value(4)
ddl.insert_at_beginning(node4)

ddl.traverse()

print("Delete position")
ddl.delete_at_position(2)
ddl.traverse()

print("Delete head")
ddl.delete_head()
ddl.traverse()

print("Delete tail")
ddl.delete_tail()
ddl.traverse()
