class stack_multi:
    def __init__(self, stacks, array_size):
        self.size = array_size
        self.tops = [None] * array_size
        self.array = [None] * array_size
