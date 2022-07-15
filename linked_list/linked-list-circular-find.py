class cyclic_node:
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


class cyclic_linked_listv2:
    def __init__(self):
        self.head = None
        self.length = 0

    def find_nth_position(self, pos):
        if pos == self.length - 1:
            return self.head
        else:
            fast = self.head
            index = 0
            while fast is not None and fast.get_next().get_value() != self.head.get_value() and pos != index:
                fast = fast.get_next()
                index = index + 1

            slow = self.head
            while fast is not None and fast.get_next().get_value() != self.head.get_value():
                slow = slow.get_next()
                fast = fast.get_next()

            print("element at position {0} from end is {1}".format(pos, slow.get_value()))

    def insert_at_beginning(self, node):
        if self.length == 0:
            node.set_next(self.head)
            self.head = node
        else:
            current = self.head
            while current is not None and current.get_next() is not None and current.get_next().get_value() != self.head.get_value():
                current = current.get_next()
            current.set_next(node)
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def insert_at_tail(self, node):
        if self.length == 0:
            self.insert_at_beginning(node)
        else:
            current = self.head
            while current is not None and current.get_next().get_value() != self.head.get_value():
                current = current.get_next()
            node.set_next(self.head)
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
            while current is not None and current.get_next().get_value() != self.head.get_value() and pos != (
                    index + 1):
                index = index + 1
                current = current.get_next()

            node.set_next(current.get_next())
            current.set_next(node)
            self.length = self.length + 1

    def traverse(self):
        current = self.head
        print(current.get_value())
        while current is not None and current.get_next().get_value() != self.head.get_value():
            current = current.get_next()
            print(current.get_value())


ddl = cyclic_linked_listv2()
cyclic1 = cyclic_node()
cyclic1.set_value(5)
ddl.insert_at_beginning(cyclic1)

cyclic2 = cyclic_node()
cyclic2.set_value(4)
ddl.insert_at_beginning(cyclic2)

cyclic3 = cyclic_node()
cyclic3.set_value(3)
ddl.insert_at_beginning(cyclic3)

cyclic4 = cyclic_node()
cyclic4.set_value(2)
ddl.insert_at_beginning(cyclic4)

cyclic5 = cyclic_node()
cyclic5.set_value(1)
ddl.insert_at_beginning(cyclic5)

cyclic6 = cyclic_node()
cyclic6.set_value(6)
ddl.insert_at_tail(cyclic6)

cyclic7 = cyclic_node()
cyclic7.set_value("0'th")
ddl.insert_at_position(0, cyclic7)

cyclic8 = cyclic_node()
cyclic8.set_value("2'th")
ddl.insert_at_position(2, cyclic8)
ddl.traverse()

ddl.find_nth_position(1)
ddl.find_nth_position(5)


