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

    # find middle
    # reverse second part (middle to end)
    # form a new list with expected result
    def rearrange_a_an_a1_an_minus_1(self):
        middle = self.find_middle()
        reversed = self.reverse(middle)

        current = self.head
        r1 = reversed

        while current is not None and r1 is not None:
            cnext = current.get_next()
            rnext = r1.get_next()
            current.set_next(r1)
            r1.set_next(cnext)
            current = cnext
            r1 = rnext

        return self.head

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.get_next()
            fast = fast.get_next().get_next()

        mid = slow.get_next()
        slow.set_next(None)
        return mid

    def reverse(self, node):
        prev = None
        current = node
        while current is not None:
            nextt = current.get_next()
            current.set_next(prev)
            prev = current
            current = nextt
        return prev

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value(), end='')
            current = current.get_next()
        print('\n ')


n1 = node()
n1.set_value(1)
n2 = node()
n2.set_value(2)
n3 = node()
n3.set_value(3)
n4 = node()
n4.set_value(4)
n5 = node()
n5.set_value(5)
n6 = node()
n6.set_value(6)
n7 = node()
n7.set_value(7)
n8 = node()
n8.set_value(8)
n9 = node()
n9.set_value(9)
ll2 = linked_list()
ll2.set_head(n9)
ll2.set_head(n8)
ll2.set_head(n7)
ll2.set_head(n6)
ll2.set_head(n5)
ll2.set_head(n4)
ll2.set_head(n3)
ll2.set_head(n2)
ll2.set_head(n1)

ll2.rearrange_a_an_a1_an_minus_1()
ll2.traverse()
