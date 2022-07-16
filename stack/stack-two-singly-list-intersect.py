class stack:
    def __init__(self, limit):
        self.limit = limit
        self.data = []

    def push(self, value):
        if self.is_full():
            print("Overflow Exception")
            return
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow Exception")
            return
        return self.data.pop()

    def is_full(self):
        return len(self.data) == self.limit

    def is_empty(self):
        return len(self.data) == 0


class node:
    def __init__(self, value):
        self.value = value
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


def find_intersection(ll1, ll2):
    if ll1 is None or ll2 is None:
        return

    stk1 = stack(20)
    stk2 = stack(20)

    current1 = ll1.get_head()
    while current1 is not None:
        stk1.push(current1)
        current1 = current1.get_next()

    current2 = ll2.get_head()
    while current2 is not None:
        stk2.push(current2)
        current2 = current2.get_next()

    pop1 = stk1.pop()
    pop2 = stk2.pop()

    while pop1 is pop2:
        pop1 = stk1.pop()
        pop2 = stk2.pop()

    print(pop1.get_value())
    print(pop2.get_value())


n10 = node(10)
n11 = node(11)
n12 = node(12)
n13 = node(13)
n14 = node(14)
n10.set_next(n11)
n11.set_next(n12)
n12.set_next(n13)
n13.set_next(n14)

n20 = node(20)
n21 = node(21)
n22 = node(22)
n23 = node(23)
n24 = node(24)
n20.set_next(n21)
n21.set_next(n22)
n22.set_next(n23)
n23.set_next(n24)

n30 = node(30)
n31 = node(31)
n32 = node(32)
n33 = node(33)
n34 = node(34)
n30.set_next(n31)
n31.set_next(n32)
n32.set_next(n33)
n33.set_next(n34)

n14.set_next(n30)
n24.set_next(n30)

ll1 = linked_list()
ll1.set_head(n10)

ll2 = linked_list()
ll2.set_head(n20)

print(n34)
find_intersection(ll1, ll2)
