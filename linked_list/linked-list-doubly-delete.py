class cnode:
    def __init__(self):
        self.value = None
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class doubly_linked_list_v1:

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        self.length = self.length + 1

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
        if pos == 0:
            self.insert_at_beginning(node)
        elif pos == self.length - 1:
            self.insert_at_tail(node)
        else:
            index = 0
            current = self.head
            while current is not None and pos != index + 1:
                current = current.get_next()

            node.set_next(current.get_next())
            current.get_next().set_prev(node)
            current.set_next(node)
            node.set_prev(current)
            self.length = self.length + 1

    def delete_head(self):
        if self.length == 0:
            print("Empty list")
        else:
            self.head = self.head.get_next()
            self.head.set_prev(None)
            self.length = self.length - 1

    def delete_at_position(self, pos):
        if pos == 0:
            self.delete_head()
        elif pos == self.length - 1:
            self.delete_tail()
        else:
            index = 0
            current = self.head
            while current is None and pos != index:
                current = current.get_next()
                index = index + 1

            prev = current.get_prev()
            nextt = current.get_next()

            prev.set_next(nextt)
            nextt.set_prev(prev)

    def delete_tail(self):
        if self.length == 0:
            print("Empty list")
        elif self.length == 1:
            self.delete_head()
        else:
            current = self.head
            while current is not None and current.get_next() is not None and current.get_next().get_next() is not None:
                current = current.get_next()
            current.set_next(None)
            self.length = self.length - 1

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


ddl = doubly_linked_list_v1()
node1 = cnode()
node1.set_value(2)
ddl.insert_at_beginning(node1)

node2 = cnode()
node2.set_value(1)
ddl.insert_at_beginning(node2)

node3 = cnode()
node3.set_value(0)
ddl.insert_at_beginning(node3)

node4 = cnode()
node4.set_value("ok")
ddl.insert_at_position(1, node4)

ddl.traverse()
print("Delete Starts")
ddl.delete_head()
ddl.delete_tail()
# ddl.delete_at_position(1)
ddl.traverse()
print("****")
ddl.traverse_reversal()
