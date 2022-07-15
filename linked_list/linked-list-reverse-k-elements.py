# Approach is known, somehow achieving it is challenge.
# Challenge is pointer, so most imp. keep next and prev pointers.

class node:
    def __init__(self, value):
        self.value = value
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

    def reverse_in_blocks(self, root, k):
        current = root
        count = 0
        prev = None
        next = None
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            root.next = self.reverse_in_blocks(next, k)

        return prev

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=' ')
            current = current.next


ll = linked_list()
ll.set_head(node(1))
ll.set_head(node(2))
ll.set_head(node(3))
ll.set_head(node(4))
ll.set_head(node(5))
ll.set_head(node(6))
ll.traverse()
result = ll.reverse_in_blocks(ll.head, 2)
ll.head = result
print("\n In blocks")
ll.traverse()
