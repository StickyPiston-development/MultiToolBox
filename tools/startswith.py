inputArray = [(' ka', ('kat ', ' auto', 'kalf', 'midden', ' k av iaar'))]

def get(inputArray):
    Startswith = "".join(filter(str.isalpha, inputArray[0][0]))
    output = []

    for i in inputArray[0][1]:
        iFiltered = "".join(filter(str.isalpha, i))
        if iFiltered.startswith(Startswith):
            output.append(iFiltered)
    return output

