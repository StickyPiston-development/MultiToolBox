def get(inputNumber):
    counter = inputNumber
    Numbers = []

    while True:
        Numbers.append(counter)
        counter += 2
        if len(Numbers) >= inputNumber:
            break
    return Numbers