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

    def length_of_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast:
            fast = fast.get_next()

            if fast is None or slow == fast:
                break

            fast = fast.get_next()
            if fast is None or slow == fast:
                break

            slow = slow.get_next()

        if slow == fast:
            length = 0
            while fast is not None and fast.get_next() is not slow:
                fast = fast.get_next()
                length = length + 1
            return length
        else:
            return 0


n1 = node()
n2 = node()
n3 = node()
n4 = node()
n5 = node()
n6 = node()
n7 = node()

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)

n6.set_next(n7)
n7.set_next(n5)
n5.set_next(n6)

ddl = linked_list()
ddl.set_head(n1)

print(ddl.length_of_loop())
