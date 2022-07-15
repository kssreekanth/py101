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


class singly_linked_list_v1:
    def __init__(self):
        self.head = None
        self.length = 0

    def set_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def get_head(self):
        return self.head

    def insert_at_end(self, node):
        if self.length == 0:
            self.head = node
        else:
            current = self.head

            while current is not None and current.get_next() is not None:
                current = current.get_next()

            current.set_next(node)
            self.length = self.length + 1

    def delete_head(self):
        self.head = self.head.get_next()
        self.length = self.length - 1

    def delete_tail(self):
        current = self.head
        while current is not None and current.get_next() is not None and current.get_next().get_next() is not None:
            current = current.get_next()
        current.set_next(None)
        self.length = self.length - 1

    def delete_at_position(self, position):
        if position == self.length - 1:
            self.delete_tail()
            self.length = self.length - 1
        elif position == 0:
            self.delete_head()
            self.length = self.length - 1
        else:
            index = 0
            current = self.get_head()
            while current is not None and index + 1 != position:
                current = current.get_next()
                index = index + 1

            to_be_deleted = current.get_next()
            if to_be_deleted is not None:
                current.set_next(to_be_deleted.get_next())
                self.length = self.length - 1

    def delete_node(self, node):
        if node is None:
            return
        if node.get_next() is None:
            node.set_value(None)
            node.set_value(None)
            return
        next = node.get_next()
        node.set_value(next.get_value())
        node.set_next(next.get_next())

    def print(self):
        current = self.get_head()
        while current is not None:
            print("Value of item is = ", current.get_value())
            current = current.get_next()


ssl = singly_linked_list_v1()
node1 = node()
node1.set_value(1)
ssl.set_head(node1)

node2 = node()
node2.set_value(2)
ssl.insert_at_end(node2)

node3 = node()
node3.set_value(3)
ssl.insert_at_end(node3)

node4 = node()
node4.set_value(4)
ssl.insert_at_end(node4)

node5 = node()
node5.set_value(5)
ssl.insert_at_end(node5)

ssl.delete_tail()
ssl.delete_tail()
ssl.delete_head()
ssl.insert_at_end(node5)
ssl.delete_tail()

ssl.insert_at_end(node4)
ssl.insert_at_end(node5)
ssl.set_head(node1)

ssl.print()
ssl.delete_at_position(2)
ssl.print()
ssl.delete_node(node5)
print("Delete a node")
ssl.print()
