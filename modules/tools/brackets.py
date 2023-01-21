def close(inputString):
    output = []
    substring = ""
    for s in inputString.replace(' ', ''):
        substring += s
        if substring.count("(") == substring.count(")"):
            output.append(substring)
            substring = ""
    return output