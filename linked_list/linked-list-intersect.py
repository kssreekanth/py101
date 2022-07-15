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

    def find_intersection(self, ll):
        if ll.length == 0:
            return None
        diff = self.length - ll.length
        first = self.head if diff >= 0 else ll.head
        second = self.head if diff < 0 else ll.head

        while first is not None and diff > 0:
            first = first.next()
            diff = diff - 1

        while first != second:
            first = first.get_next()
            second = second.get_next()

        return first


i1 = node()
i2 = node()
i3 = node()
i1.set_next(i2)
i2.set_next(i3)

n1 = node()
n2 = node()
n3 = node()
n4 = node()
n5 = node()

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(i1)
ddl = linked_list()
ddl.set_head(n1)

m1 = node()
m2 = node()
m3 = node()
m4 = node()
m5 = node()

m1.set_next(m2)
m2.set_next(m3)
m3.set_next(m4)
m4.set_next(m5)
m5.set_next(i1)
ddl1 = linked_list()
ddl1.set_head(m1)

print(ddl.find_intersection(ddl1))
print(i1)
