def is_array_sorted(input):
    if len(input) == 0:
        print("Input is empty")
        return
    index = 0
    print(input)
    while index < len(input) - 1:
        if input[index] > input[index + 1]:
            print("Array is not sorted")
            return
        index = index + 1
    print("Array is sorted")


def is_array_sorted1(input):
    if len(input) == 1:
        return True
    return input[0] < input[1] and is_array_sorted1(input[1:])


def is_array_sorted2(input):
    if len(input) == 0:
        print("Empty array")
    if is_array_sorted2_helper(input, len(input), 0):
        print("Array is sorted")
    else:
        print("Array is not sorted")


def is_array_sorted2_helper(input, length, index):
    if index == length - 1:
        return True
    return input[index] < input[index + 1] and is_array_sorted2_helper(input, length, index + 1)


is_array_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])
is_array_sorted([9, 2, 3, 4, 5, 6, 7, 8, 9])

print(is_array_sorted1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(is_array_sorted1([9, 2, 3, 4, 5, 6, 7, 8, 9]))

is_array_sorted2([1, 2, 3, 4, 5, 6, 7, 8, 9])
is_array_sorted2([1, 2, 3, 4, 3, 6, 7, 8, 9])
