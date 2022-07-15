class node:
    def __init__(self):
        self.value = None
        self.next = None


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

    def find_middle(self):
        if self.length == 0:
            return None
        middle = self.length / 2
        current = self.head
        while current is not None and middle > 0:
            current = current.next
            middle = middle - 1
        return current

    def find_middlev1(self):
        slow = self.head
        fast = slow.next
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow


n1 = node()
n2 = node()
n3 = node()
n4 = node()
n5 = node()
n6 = node()

ddl = linked_list()
ddl.set_head(n1)
ddl.set_head(n2)
ddl.set_head(n3)
ddl.set_head(n4)
ddl.set_head(n5)
ddl.set_head(n6)

print(ddl.find_middle())
print(n3)

print(ddl.find_middlev1())
print(n3)
