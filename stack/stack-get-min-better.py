class stack_min:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, value):
        if len(self.min) == 0 or self.min[-1] > value:
            self.min.append(value)
        self.data.append(value)

    def pop(self):
        popped = self.data.pop()
        if popped == self.min[-1]:
            self.min.pop()
        return popped

    def get_min(self):
        return self.min[-1]

st = stack_min()
st.push(10)
st.push(1)
st.push(11)
st.push(2)
st.push(0)
st.push(5)

st.pop()

print(st.get_min())