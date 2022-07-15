class cnode:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def set_prev(self, node):
        self.prev = node

    def get_prev(self):
        return self.prev


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        if self.length == 0:
            return self.head
        else:
            return None

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        self.length = self.length + 1

    def insert_at_beginning(self, node):
        self.set_head(node)

    def insert_at_tail(self, node):
        if self.length == 0:
            self.insert_at_beginning(node)
        else:
            current = self.head
            while current is not None and current.get_next() is not None:
                current = current.get_next()

            node.set_prev(current)
            current.set_next(node)
            self.length = self.length + 1

    def insert_at_position(self, pos, node):
        if pos > self.length - 1:
            print("Invalid position")
        elif pos == 0:
            self.insert_at_beginning(node)
        elif pos == self.length - 1:
            self.insert_at_tail(node)
        else:
            index = 0
            current = self.head
            while current is not None and pos != index + 1:
                index = index + 1
                current = current.get_next()

            node.set_next(current.get_next())
            current.get_next().set_prev(node)
            current.set_next(node)
            node.set_prev(current)

            self.length = self.length + 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()

    def traverse_reversal(self):
        current = self.head
        while current is not None and current.get_next() is not None:
            current = current.get_next()

        while current is not None:
            print(current.get_value())
            current = current.get_prev()


dll = doubly_linked_list()
cnode1 = cnode()
cnode1.set_value(4)
dll.set_head(cnode1)

cnode2 = cnode()
cnode2.set_value(3)
dll.set_head(cnode2)

cnode3 = cnode()
cnode3.set_value(2)
dll.set_head(cnode3)

cnode4 = cnode()
cnode4.set_value(1)
dll.set_head(cnode4)

cnode5 = cnode()
cnode5.set_value(0)
dll.set_head(cnode5)

tail = cnode()
tail.set_value("end")
dll.insert_at_tail(tail)

pos0node = cnode()
pos0node.set_value("pos0")
dll.insert_at_position(0, pos0node)

pos1node = cnode()
pos1node.set_value("pos1")
dll.insert_at_position(1, pos1node)

pos3node = cnode()
pos3node.set_value("pos3")
dll.insert_at_position(3, pos3node)

dll.traverse()
print("****")
dll.traverse_reversal()
