def generate_binary_string(n, result):
    if n == 0:
        print(result)
        return

    generate_binary_string(n - 1, result + "0")
    generate_binary_string(n - 1, result + "1")


def generate_by_base(base, cutoff, result):
    if cutoff == 0:
        print(result)
        return
    for i in range(0, base):
        generate_by_base(base, cutoff - 1, result + str(i))

generate_binary_string(3, "")
print("***")
generate_by_base(2, 2, "")
print("***")
generate_by_base(3, 3, "")
print("***")
generate_by_base(3, 1, "")  # base 3 of 1 length.
