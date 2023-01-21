def get(InputArray):
    output = (InputArray[len(InputArray)-1]).find(InputArray[len(InputArray)-2]) != -1
    return output