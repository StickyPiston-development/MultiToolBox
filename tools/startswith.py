def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending,flush=True)

inputArray = [(' ka', ('kat ', ' auto', 'kalf', 'midden', ' k av iaar'))]

Startswith = "".join(filter(str.isalpha, inputArray[0][0]))
print("Returning strings starting with: " + Startswith)

for i in inputArray[0][1]:
    iFiltered = "".join(filter(str.isalpha, i))
    progress_bar(inputArray[0][1].index(i), len(inputArray[0][1]))
    #if iFiltered.startswith(Startswith):
    #    print(iFiltered)
    