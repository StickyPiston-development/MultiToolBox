def get(numbers):
    if len(numbers) != 100:
        return[False, None, None, "Invalid array size"]
    difference = abs(numbers[0]-numbers[1])

    for i in range(len(numbers)):
        if not abs(numbers[i]-numbers[i-1]) == difference and not i == 0 or not isinstance(i, int):
            return[False, i + 1, numbers[i], "Number does not have the same distance between."]
    return[True, None, None, "Number meets all criteria"]