import math


def logarithm(number):
    log = 0
    result = number
    while result > 1:
        result = math.floor(result / 2)
        log = log + 1

    print(log)


def logarithm1(number):
    log = 0
    temp = 1
    while temp < number:
        temp = temp * 2
        log = log + 1

    print(log)


logarithm(1)
logarithm(2)
logarithm(8)
logarithm(10)
logarithm(16)
print("***********")
logarithm1(1)
logarithm1(2)
logarithm1(8)
logarithm1(10)
logarithm1(16)
