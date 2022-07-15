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

    def is_palindrome(self):

        # not a good approach , we change LL pointers just for a check. Best option.

        if self.length == 0:
            return None

        if self.length == 1:
            return True

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.get_next()
            fast = fast.get_next().get_next()

        second = slow.get_next()
        slow.set_next(None)
        first = self.head

        # reverse second, to be honest it does not make sense.
        prev = None
        current = second
        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next

        second = prev

        while first and second:
            if first.get_value() is not second.get_value():
                return False
            else:
                first = first.get_next()
                second = second.get_next()

        return True

    def reverse(self):
        if self.length == 0:
            return None

        current = self.head
        prev = None

        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next

        self.head = prev

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

n5 = node()
n5.set_value(2)

n6 = node()
n6.set_value(1)

ll = linked_list()
ll.set_head(n6)
ll.set_head(n5)
ll.set_head(n3)
ll.set_head(n2)
ll.set_head(n1)
ll.traverse()
print(ll.is_palindrome())
