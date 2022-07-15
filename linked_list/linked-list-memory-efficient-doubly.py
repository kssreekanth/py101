import ctypes


class mnode:
    def __init__(self):
        self.data = None
        self.next_prev = None

    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value

    def set_next_prev(self, next, prev):
        self.next_prev = id(next) ^ id(prev)

    def get_next(self, prev):
        return self.next_prev ^ id(prev)

    def get_prev(self, next):
        return self.next_prev ^ id(next)


class memory_doubly_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def set_head(self, node):
        if self.length == 0:
            node.set_next_prev(None, None)
            self.head = node
        else:
            current_head = self.head
            prev = None
            next_id = current_head.get_next(prev)
            next = ctypes.cast(next_id, ctypes.py_object).value
            current_head.set_next_prev(next, node)
            node.set_next_prev(current_head, None)
            self.head = node
        self.length = self.length + 1

    def insert_at_beginning(self, node):
        self.set_head(node)

    def insert_at_tail(self, node):

        if self.length == 0:
            self.set_head(node)
        else:
            prev = None
            current = self.head
            next_id = current.get_next(prev)
            next = ctypes.cast(next_id, ctypes.py_object).value

            while current is not None and next is not None:
                next_id = next.get_next(current)
                current = next
                next = ctypes.cast(next_id, ctypes.py_object).value

            tail_prev_id = current.get_prev(None)
            tail_prev = ctypes.cast(tail_prev_id, ctypes.py_object).value
            current.set_next_prev(node, tail_prev)
            node.set_next_prev(None, current)
            self.length = self.length + 1

    def delete_head(self):
        if self.length == 0:
            self.head = None
        else:
            next_id = self.head.get_next(None)
            next = ctypes.cast(next_id, ctypes.py_object).value
            next_next_id = next.get_next(self.head)
            next_next = ctypes.cast(next_next_id, ctypes.py_object).value
            next.set_next_prev(next_next, None)
            self.head = next

    def delete_tail(self):
        if self.length == 0:
            self.head = None
        else:
            prev = None
            current = self.head
            next_id = self.head.get_next(None)
            next = ctypes.cast(next_id, ctypes.py_object).value
            while current is not None and next is not None:
                next_id = next.get_next(current)
                current = next
                next = ctypes.cast(next_id, ctypes.py_object).value

            prev_id = current.get_prev(None)
            prev = ctypes.cast(prev_id, ctypes.py_object).value
            prev_prev_id = prev.get_prev(current)
            prev_prev = ctypes.cast(prev_prev_id, ctypes.py_object).value
            prev.set_next_prev(None, prev_prev)

    def traverse(self):
        prev = None
        current = self.head
        while current is not None:
            print(current.get_data())
            next_id = current.get_next(prev)
            prev = current
            current = ctypes.cast(next_id, ctypes.py_object).value


ddl = memory_doubly_linked_list()
m1 = mnode()
m1.set_data(1)
ddl.set_head(m1)

m2 = mnode()
m2.set_data(2)
ddl.set_head(m2)

m3 = mnode()
m3.set_data(0)
ddl.insert_at_tail(m3)

m4 = mnode()
m4.set_data(-1)
ddl.insert_at_tail(m4)

ddl.delete_head()
ddl.delete_head()

ddl.delete_tail()
ddl.delete_tail()

ddl.traverse()
