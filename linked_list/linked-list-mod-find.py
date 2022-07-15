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

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()

    # index 0 approach
    def find_last_mod_of_ok(self, k):
        mode_node = None
        current = self.head
        for i in range(0, self.length - 1):
            if i % k == 0:
                mode_node = current
            current = current.get_next()
        return mode_node

    def find_last_mod_of_k_v1(self, k):
        index = 1
        current = self.head
        mode_node = None
        while current is not None:
            if index % k == 0:
                mode_node = current

            index = index + 1
            current = current.get_next()
        return mode_node

    # basically both mod are of same in nature, find nth element from last. Since its index based.
    def find_first_mode_of_from_end(self, k):
        index = 0
        current = self.head
        mode_node = self.head
        while index < k and current is not None:
            current = current.get_next()
            index = index + 1

        while current is not None:
            current = current.get_next()
            mode_node = mode_node.get_next()

        return mode_node

    # 10/2 -> 5th element. If length is not present?
    # 1 2 3 4 5 6 7 8 9 10
    def find_fraction_n(self, k):
        current = self.head
        index = 1
        fraction_node = None
        while current is not None:
            if index % k == 0:
                if fraction_node is None:
                    fraction_node = self.head
                else:
                    fraction_node = fraction_node.get_next()
            index = index + 1
            current = current.get_next()
        return fraction_node

    def root_of_n_node(self):
        current = self.head
        roo_node = None
        index = 1
        mul = 1
        while current is not None:
            if index == mul * mul:
                if roo_node is None:
                    roo_node = self.head
                else:
                    roo_node = roo_node.get_next()
                mul = mul + 1
            index = index + 1
            current = current.get_next()
        return roo_node


ll = linked_list()
ll.set_head(node(1))
ll.set_head(node(2))
ll.set_head(node(3))
ll.set_head(node(4))
ll.set_head(node(5))
ll.set_head(node(6))
ll.set_head(node(7))
ll.set_head(node(8))
ll.set_head(node(9))
ll.traverse()

# 5 4 3 2 1
# 0 1 2 3 4 - Correct when index start with 0
# 1 2 3 4 5 - Correct when index start with 1
result = ll.find_last_mod_of_ok(2)
print(result.get_value())
result1 = ll.find_last_mod_of_k_v1(2)
print(result1.get_value())
result2 = ll.find_first_mode_of_from_end(2)
print(result2.get_value())
result3 = ll.find_fraction_n(3)
print(result3.get_value())
result4 = ll.root_of_n_node()
print(result4.get_value())
