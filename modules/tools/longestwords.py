def get(inputString):
    words = inputString.split()
    maxlength = len(max(words, key=len))

    result = [textword for textword in words if len(textword) == maxlength]

    return[maxlength, result]