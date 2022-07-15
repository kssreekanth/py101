class node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


class singly_linked_list_v2:
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

    def get_head(self):
        return self.head

    def insert_at_beginning(self, node):
        self.set_head(node)

    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current is not None and current.get_next() is not None:
                current = current.get_next()

            current.set_next(node)
        self.length = self.length + 1

    def insert_at_position(self, pos, node):
        if pos > self.length:
            return
        if pos == 0:
            self.set_head(node)
        elif pos == self.length - 1:
            self.insert_at_end(node)
        else:
            current = self.head
            index = 0
            while current is not None and (index + 1) != pos:
                current = current.get_next()
                index = index + 1

            self.length = self.length + 1
            node.set_next(current.get_next())
            current.set_next(node)

    def print(self):
        current = self.head
        index = 0
        while current is not None:
            print("Position =", index, ": Value = ", current.get_value())
            current = current.get_next()
            index = index + 1

    def find_nth_from_end(self, pos):
        if pos == self.length - 1:
            return self.head
        else:
            find_pos = (self.length - 1) - pos
            current = self.head
            index = 0
            while current is not None and index != find_pos:
                index = index + 1
                current = current.get_next()
            return current

    def find_nth_from_end_v1(self, pos):
        if pos == self.length - 1:
            return self.get_head()
        else:
            fast = self.head
            index = 0
            while fast is not None and index != pos:
                fast = fast.get_next()
                index = index + 1

            slow = self.head
            while fast is not None and fast.get_next() is not None:
                fast = fast.get_next()
                slow = slow.get_next()
            return slow


sll = singly_linked_list_v2()
sll.set_head(node(1, None))
sll.set_head(node(0, None))
sll.insert_at_beginning(node(-1, None))
sll.insert_at_end(node(2, None))
sll.insert_at_position(4, node(4, None))
sll.print()
print(sll.find_nth_from_end(1).get_value())
print(sll.find_nth_from_end_v1(1).get_value())
print(sll.find_nth_from_end_v1(0).get_value())
print(sll.find_nth_from_end_v1(2).get_value())
