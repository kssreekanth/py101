class node:

    def __init__(self):
        self.__value = None
        self.__next = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next


class singly_linked_list:
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

    def insert_at_beginning(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def insert_at_end(self, node):
        if self.length == 0:
            self.head = node
        else:
            current = self.head
            while current is not None and current.get_next() is not None:
                current = current.get_next()
        current.set_next(node)
        self.length = self.length + 1

    def insert_at_position(self, position, node):
        if position == 0:
            self.insert_at_beginning(node)
        elif position == self.length - 1:
            self.insert_at_end(node)
        else:
            current = self.head
            # 0 1 [2] 3 4 5
            index = 0
            while current is not None and (index + 1) != position:
                index = index + 1
                current = current.get_next()
            print("Index is {0}, position {1}".format(index, position))
            next_of_current = current.get_next()
            node.set_next(next_of_current)
            current.set_next(node)
            self.length = self.length + 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()


sll1 = singly_linked_list()

node2 = node()
node2.set_value(2)
sll1.set_head(node2)

node1 = node()
node1.set_value(1)
sll1.insert_at_beginning(node1)

node3 = node()
node3.set_value(3)
sll1.insert_at_end(node3)

node4 = node()
node4.set_value(4)
sll1.insert_at_end(node4)

node5 = node()
node5.set_value(5)

sll1.insert_at_position(0, node5)

sll1.print()

node6 = node()
node6.set_value(6)

sll1.insert_at_position(2, node6)

sll1.print()
