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

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast:
            fast = fast.get_next()

            if slow == fast:
                return True

            if fast is None:
                return False

            fast = fast.get_next()
            if slow == fast:
                return True

            slow = slow.get_next()


n1 = node()
n2 = node()
n3 = node()
n4 = node()
n5 = node()

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n1)

ddl = linked_list()
ddl.set_head(n1)

print(ddl.detect_loop())
