import modules

def read_tools():
    with open('tools.txt', 'r') as toolFile:
        toolList = ''.join(toolFile.readlines())
        return toolList

def menu():
    print("\033[H\033[J", end="")
    toolList = read_tools().split('\n')

    print(modules.logo.ascii("multitoolbox"))
    print("+-----------------------------------------+\n| Number | Tool name            | Version |\n+-----------------------------------------+")
    for i in toolList:
        iSplit = i.split('|')
        print(f'| {str(toolList.index(i) + 1)}\t | {iSplit[0]} | {iSplit[1]}     |')
    toolInput(input("+-----------------------------------------+\n\nEnter a tool number or exit to exit: "), toolList)

def toolInput(toolNumber, toolList):
    if toolNumber.lower() == "exit":
        exit()
    try:
        toolNumber = int(toolNumber)
    except ValueError:
        toolInput(input("\nPlease enter a valid tool number: "), toolList)
        return
    if toolNumber > len(toolList):
        toolInput(input("\nPlease enter a valid tool number: "), toolList)
        return
    
    tool = "".join(filter(str.isalpha, toolList[toolNumber-1].split('|')[0].lower()))

    print("\033[H\033[J", end="")
    print(modules.logo.ascii(tool))

    match toolList[toolNumber-1].split('|')[2]:
        case "int":
            modules.input.integer(toolNumber)
        case "flo":
            modules.input.flo(toolNumber)
        case "str":
            modules.input.string(toolNumber)
        case "arr":
            modules.input.array(toolNumber)

if __name__ == "__main__":
    while True:
        menu()
