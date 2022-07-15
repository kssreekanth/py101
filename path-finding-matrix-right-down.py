def path_finder(input, start, destination, path):
    if start == (destination - 1, destination - 1):
        print(path)
        return
    x, y = start
    if x + 1 < destination and input[x + 1][y] == 1:
        path = path + ',' + ''.join(map(str, (x + 1, y)))
        path_finder(input, (x + 1, y), destination, path)

    if y + 1 < destination and input[x][y + 1] == 1:
        path = path + ',' + ''.join(map(str, (x, y + 1)))
        path_finder(input, (x, y + 1), destination, path)

    path = ""


input = [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [1, 0, 1, 1, 1]]
path_finder(input, (0, 0), 5, "")

# [1, 1, 1, 1, 0]
# [0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0]
# [0, 1, 1, 0, 0]
# [1, 0, 1, 1, 1]
