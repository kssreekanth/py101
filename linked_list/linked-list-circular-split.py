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


class circular_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def set_head(self, node):
        if self.length == 0:
            node.set_next(node)
            self.head = node
        else:
            current = self.head
            while current is not None and current.get_next() is not self.head:
                current = current.get_next()
            current.set_next(node)
            node.set_next(self.head)
            self.head = node

        self.length = self.length + 1

    def traverse(self):
        current = self.head
        print(current.get_value())
        while current is not None and current.get_next() is not self.head:
            current = current.get_next()
            print(current.get_value())

    def split(self):

        # find middle : we have length stored, we could easily do it, but try 2x approach
        slow = self.head
        fast = self.head
        middle = None
        prev = None

        while slow and fast:
            fast = fast.get_next()
            if fast == self.head:
                break

            prev = fast

            fast = fast.get_next()
            if fast == self.head:
                break

            prev = fast
            slow = slow.get_next()

        if fast is self.head:
            middle = slow.get_next()
            slow.set_next(None)
            prev.next = None

        return self.head, middle


ll = circular_linked_list()
n1 = node()
n1.set_value(1)
ll.set_head(n1)

n2 = node()
n2.set_value(2)
ll.set_head(n2)

n3 = node()
n3.set_value(3)
ll.set_head(n3)

n4 = node()
n4.set_value(4)
ll.set_head(n4)

n5 = node()
n5.set_value(5)
ll.set_head(n5)

ll.traverse()

print("First")

first, second = ll.split()
f = first
while f is not None:
    print(f.get_value())
    f = f.get_next()

print("Second")
s = second
while s is not None:
    print(s.get_value())
    s = s.get_next()
