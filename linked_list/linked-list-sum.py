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
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def sum_of_values(self):
        return self.sum_helper(self.head, 0)

    def sum_helper(self, node, sum):
        if node is None:
            return sum
        return self.sum_helper(node.get_next(), sum + node.get_value())


ll = linked_list()
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

print(ll.sum_of_values())
