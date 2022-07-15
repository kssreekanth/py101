class stack_minimum:
    def __init__(self, limit):
        self.limit = limit
        self.data = []
        self.min = []

    def push(self, value):
        if self.is_full():
            print("Overflow")
            return

        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)
        else:
            self.min.append(self.min[-1])

        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow")
            return

        self.min.pop()
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_full(self):
        return len(self.data) == self.limit

    def is_empty(self):
        return len(self.data) == 0

    def get_minimum(self):
        return self.min[-1]


st = stack_minimum(10)
st.push(10)
st.push(1)
st.push(11)
st.push(2)
st.push(0)
st.push(5)

st.pop()
st.pop()
print(st.get_minimum())
