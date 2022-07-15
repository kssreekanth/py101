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

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.head = prev

    def reverse_recursive(self):
        if self.head is None:
            return None
        if self.length == 0:
            return self.head
        self.head = self.reverse_helper(None, self.head)

    def reverse_helper(self, prev, n):
        if n is None:
            return prev
        next = n.get_next()
        n.set_next(prev)
        prev = n
        n = next
        return self.reverse_helper(prev, n)

    def print_reverse(self):
        if self.length == 0:
            print(None)
        else:
            result = self.print_reverse_helper(self.head, "")
            print(result)

    def print_reverse_helper(self, node, track):
        if node is None:
            return track
        track = str(node.get_value()) + track
        return self.print_reverse_helper(node.get_next(), track)

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()


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
ll.traverse()
ll.print_reverse()
