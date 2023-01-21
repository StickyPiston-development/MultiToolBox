def check(inputNumber):
    output = inputNumber >= 256 and inputNumber % 34 == 4
    return output

def find(inputNumber):
    solutionA = False
    solutionB = False
    a = inputNumber
    b = inputNumber
        
    while not solutionA and not solutionB:
        a += 1
        b -= 1

        solutionA = a >= 256 and a % 34 == 4
        solutionB = b >= 256 and b % 34 == 4

    if solutionA:
        return a
    elif solutionB:
        return b
    else:
        # This should not happen
        print("\033[91mERROR, number not found\033[0m")
        return 0