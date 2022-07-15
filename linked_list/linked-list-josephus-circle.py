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


class circular_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def set_head(self, node):
        if self.length == 0:
            node.set_next(node)
            self.head = node
        else:
            current = self.head
            while current is not None and current.get_next() is not self.head:
                current = current.get_next()
            current.set_next(node)
            node.set_next(self.head)
            self.head = node

        self.length = self.length + 1

    # node to be deleted at cycle
    def josephus_circle(self, m):
        deleted = []
        current = self.head
        prev = None
        index = 0
        while current is not None and current.get_next() != current:
            index = index + 1
            if index == m:
                prev.set_next(current.get_next())
                deleted.append(current.get_value())
                index = 0

            prev = current
            current = current.get_next()

        return deleted, current


n1 = node()
n1.set_value(1)

n2 = node()
n2.set_value(2)

n3 = node()
n3.set_value(3)

n4 = node()
n4.set_value(4)

ll = circular_linked_list()
ll.set_head(n1)
ll.set_head(n2)
ll.set_head(n3)
ll.set_head(n4)
# 4->3->2>-1 : [3] 4->2-1 -> [3,1] 2->4 -> [3,1,2] 4
deleted, saved = ll.josephus_circle(2)
print(str(deleted))
print(saved.get_value())
