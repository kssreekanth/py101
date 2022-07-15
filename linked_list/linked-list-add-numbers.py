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

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value(), end=' ')
            current = current.get_next()
        print("\n")

    # left to right addition simple. Not the correct way.
    def add(self, l1, l2):

        longer = l1.head if l1.length > l2.length else l2.head
        shorter = l1.head if l1.length <= l2.length else l2.head
        current_long = longer
        current_short = shorter

        root = node()
        result = root
        carry = 0
        while current_long is not None:
            short_value = 0 if current_short is None else current_short.get_value()
            sum = current_long.get_value() + short_value + carry

            carry = 1 if sum >= 10 else 0
            value = sum % 10

            n1 = node()
            n1.set_value(value)
            result.set_next(n1)
            result = result.get_next()

            current_short = None if current_short is None else current_short.get_next()
            current_long = current_long.get_next()

        if carry == 1:
            n1 = node()
            n1.set_value(1)
            result.set_next(n1)

        llr = linked_list()
        llr.head = root.get_next()
        return llr

    def add_v1(self, l1, l2):
        while l1.length != l2.length:
            if l1.length > l2.length:
                n0 = node()
                n0.set_value(0)
                l2.set_head(n0)

            if l1.length < l2.length:
                n0 = node()
                n0.set_value(0)
                l1.set_head(n0)

        result = linked_list()
        carry = self.add_recursive(l1.head, l2.head, result)

        if carry > 0:
            n1 = node()
            n1.set_value(carry)
            result.set_head(n1)

        return result

    def add_recursive(self, l1, l2, result):

        if l1 is None or l2 is None:
            return 0

        sum = l1.get_value() + l2.get_value() + self.add_recursive(l1.get_next(), l2.get_next(), result)

        value = sum % 10
        n1 = node()
        n1.set_value(value)
        result.set_head(n1)
        carry = 1 if sum >= 10 else 0

        return carry


n1 = node()
n1.set_value(1)
n2 = node()
n2.set_value(2)
n3 = node()
n3.set_value(3)
ll1 = linked_list()
ll1.set_head(n3)
ll1.set_head(n2)
ll1.set_head(n1)

n6 = node()
n6.set_value(6)
n7 = node()
n7.set_value(7)
n8 = node()
n8.set_value(5)
n9 = node()
n9.set_value(9)
ll2 = linked_list()
ll2.set_head(n6)
ll2.set_head(n7)
ll2.set_head(n8)
ll2.set_head(n9)

lladd = linked_list()
ll1.traverse()
ll2.traverse()
lr = lladd.add(ll1, ll2)
lr.traverse()

lr1 = lladd.add_v1(ll1, ll2)
lr1.traverse()
