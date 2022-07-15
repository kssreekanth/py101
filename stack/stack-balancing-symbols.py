class stack:
    def __init__(self, limit):
        self.limit = limit
        self.data = []

    def push(self, value):
        if self.is_full():
            print("Overflow exception")
            return

        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow exception")
            return

        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.limit


def check_balancing_symbols(input):
    if input is None:
        return

    stack_symbols = stack(100)
    symbols = {'{': '}', '[': ']', '(': ')'}
    balanced = 0
    for symbol in input:
        if symbols.get(symbol) is not None:
            stack_symbols.push(symbol)
        else:
            if stack_symbols.is_empty():
                balanced = 0
            else:
                poped = stack_symbols.pop()
                if symbols.get(poped) is not symbol:
                    balanced = 0
                else:
                    balanced = 1
    return balanced


print(check_balancing_symbols("[())]"))
