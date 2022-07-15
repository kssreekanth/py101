class node:
    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class singly_linked_list:
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


def find_intersection(ll1, ll2):
    diff = ll1.length - ll2.length
    if diff >= 0:
        first = ll1
        second = ll2
    else:
        first = ll2
        second = ll1

    first_pointer = first.head
    index = 0
    while first_pointer is not None and index != diff:
        first_pointer = first_pointer.get_next()
        index = index + 1

    second_pointer = second.head
    while first_pointer != second_pointer:
        first_pointer = first_pointer.get_next()
        second_pointer = second_pointer.get_next()

    return first_pointer


def find_intersection_stack():
    print("God")

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
ddl1 = singly_linked_list()
ddl1.set_head(n1)

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
ddl2 = singly_linked_list()
ddl2.set_head(m1)

resul = find_intersection(ddl1, ddl2)
print(resul)
