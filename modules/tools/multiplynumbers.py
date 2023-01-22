from math import prod

def odd(inputNumber):
    total = []
    for i in str(inputNumber):
        if int(i) % 2 == 1:
            total.append(int(i))
    return prod(total)
def even(inputNumber):
    total = []
    for i in str(inputNumber):
        if int(i) % 2 != 1:
            total.append(int(i))
    return prod(total)