import modules

def integer(toolNumber):
    InputNumber = input("Enter a number or enter exit to exit:\n\n")
    while True:
        if InputNumber == 'exit':
            return
        elif not InputNumber.isdigit():
            print("Please enter a valid number.")
        else:
            print(modules.tool.run(toolNumber, int(InputNumber)))
        InputNumber = input("\n")

def flo(toolNumber):
    InputNumber = input("Enter a number or enter exit to exit:\n\n")
    while True:
        if InputNumber == 'exit':
            return
        try:
            InputNumber = float(InputNumber)
            print(modules.tool.run(toolNumber, InputNumber))
        except Exception as E:
            print("Please enter a valid number.\n" + str(E))
        InputNumber = input("\n")

def string(toolNumber):
    InputString = input("Enter a string or enter exit to exit:\n\n")
    while True:
        if InputString == "exit":
            return
        else:
            print(modules.tool.run(toolNumber, InputString))
        InputString = input("\n")

def array(toolNumber):
    InputArray = input("Enter a array or enter exit to exit:\n\n")
    while True:
        if InputArray == "exit":
            return
        try:
            InputArray = eval(InputArray)
        except Exception as E:
            print("An unexpected error occurred:\n" + str(E))
        if type(InputArray) == list:
            print(modules.tool.run(toolNumber, InputArray))
        InputArray = input("\n")

#InputArray = [int(i) for i in InputArray]