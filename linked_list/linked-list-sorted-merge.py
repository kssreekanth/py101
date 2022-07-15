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

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length = self.length + 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def merge_sorted_ll(self, ll):
        new = node()
        pointer = new
        l1 = self.head
        l2 = ll.head

        # 5 4 3 2 1 + # 10 9 8 7 6
        while l1 and l2:

            if l1.get_value() > l2.get_value():
                next = l1.get_next()
                pointer.set_next(l1)
                l1 = next
            else:
                next = l2.get_next()
                pointer.set_next(l2)
                l2 = next

            pointer = pointer.get_next()

        if l2 is None:
            pointer.set_next(l1)

        if l1 is None:
            pointer.set_next(l2)

        llr = linked_list()
        llr.set_head(new.get_next())
        return llr

    def merge_sorted_llv1(self, ll):

        if self.length == 0:
            return ll

        if ll.length == 0:
            return self

        l1 = self.head
        l2 = ll.head

        new_node = node()
        pointer = new_node

        while l1 and l2:

            if l1.get_value() > l2.get_value():
                pointer.set_next(l1)
                l1 = l1.get_next()
            else:
                pointer.set_next(l2)
                l2 = l2.get_next()

            pointer = pointer.get_next()

        if l1 is None:
            pointer.set_next(l2)

        if l2 is None:
            pointer.set_next(l1)

        ll3 = linked_list()
        ll3.set_head(new_node)
        return ll3


n1 = node()
n1.set_value(1)

n2 = node()
n2.set_value(2)

n3 = node()
n3.set_value(3)

n4 = node()
n4.set_value(4)

ll = linked_list()
ll.set_head(n1)
ll.set_head(n2)
ll.set_head(n3)
ll.set_head(n4)

m1 = node()
m1.set_value(5)

m2 = node()
m2.set_value(6)

m3 = node()
m3.set_value(7)

m4 = node()
m4.set_value(8)

ll1 = linked_list()
ll1.set_head(m1)
ll1.set_head(m2)
ll1.set_head(m3)
ll1.set_head(m4)

result = ll.merge_sorted_llv1(ll1)
result.traverse()
