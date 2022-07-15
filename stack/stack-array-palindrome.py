# basically if first and last are matching its palindrome

def is_palindrome(input, start_index, end_index):
    if start_index == end_index:
        return True
    return input[start_index] == input[end_index] and is_palindrome(input, start_index + 1, end_index - 1)


input = ['M', 'A', 'L', 'A', 'Y', 'A', 'L', 'A', 'M']
print(is_palindrome(input, 0, len(input) - 1))


class stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()


def is_palindrome_v1(input):
    if len(input) == 0:
        return

    stk = stack()
    for char in input:
        stk.push(char)

    for char in input:
        if char != stk.pop():
            return False

    return True


input = ['M', 'A', 'L', 'A', 'Y', 'A', 'L', 'A', 'M']
print(is_palindrome_v1(input))
