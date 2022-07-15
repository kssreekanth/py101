class node:
    def __init__(self):
        self.value = None
        self.next = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


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

    def get_head(self):
        return self.head

    def find_start_of_loop(self):
        # If list is empty or has only one node
        # without loop
        if (self.head == None or self.head.next == None):
            return None

        slow = self.head
        fast = self.head

        # Move slow and fast 1 and 2 steps
        # ahead respectively.
        slow = slow.next
        fast = fast.next.next

        # Search for loop using slow and
        # fast pointers
        while (fast and fast.next):
            if (slow == fast):
                break

            slow = slow.next
            fast = fast.next.next

        # If loop does not exist
        if (slow != fast):
            return None

        print(slow.get_value())
        print(fast.get_value())

        # If loop exists. Start slow from
        # head and fast from meeting point.
        slow = self.head

        while (slow != fast):
            slow = slow.next
            fast = fast.next

        return slow


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

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)
n6.set_next(n7)
n7.set_next(n6)

ddl = linked_list()
ddl.head = n1
ddl.head.next = n2
ddl.head.next.next = n3
ddl.head.next.next.next = n4
ddl.head.next.next.next.next = n5

# Create a loop for testing
ddl.head.next.next.next.next.next = n3

print(ddl.find_start_of_loop().get_value())
