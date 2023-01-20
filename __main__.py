import tools

tools.startswith.progress_bar()

def read_tools():
    with open('tools.txt', 'r') as toolFile:
        toolList = ''.join(toolFile.readlines())
        return toolList

def menu():
    toolList = read_tools().split('\n')

    print(ascii("multitoolbox"))
    print("+-----------------------------------------+\n| Number | Tool name            | Version |\n+-----------------------------------------+")
    for i in toolList:
        iSplit = i.split('v.')
        print(f'| {str(toolList.index(i) + 1)}      | {iSplit[0]} | {iSplit[1]}     |')
    input("+-----------------------------------------+\n\nEnter a tool number:")




if __name__ == "__main__":
    menu()
