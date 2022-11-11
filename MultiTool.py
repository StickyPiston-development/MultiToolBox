ToolKitVersion = "0.3"

Tool = ""

def Tools():
    # Tool list (Nested)
    Tools = [
        ["CriteriaChecker", 0.1], 
        ["CriteriaChecker", 0.2],
        ["NumberArray", 0.1],
        ["SequenceChecker", 0.1]]

    # Print tool + version
    for i, tool in enumerate(Tools):
        print("(" + str(i+1) + ")   " + str(tool[0]) + "\t v. " + str(tool[1]))

    # Verify success
    return True

# CriteriaChecker
def CriteriaChecker_Check(Number):
    output = Number >= 256 and Number % 34 == 4
    print("Number meets the requirements: " + str(output) + "\n")

    return output

def CriteriaChecker_Find(Number):
    solutionA = False
    solutionB = False
    a = inputNumber
    b = inputNumber
        
    while not solutionA and not solutionB:
        a += 1
        b -= 1

        solutionA = a >= 256 and a % 34 == 4
        solutionB = b >= 256 and b % 34 == 4

    if solutionA:
        print("The nearest number that meets the criteria is: " + str(a) + "\n")
        return solutionA
    elif solutionB:
        print("The nearest number that meets the criteria is: " + str(b) + "\n")
        return solutionB
    else:
        # This should not happen
        print("\033[91mERROR, number not found\033[0m")
        return 0

# NumberArray
def NumberArray(Number):
    counter = Number
    Numbers = []

    while True:
        
        Numbers.append(counter)
        counter += 2
        if len(Numbers) >= inputNumber:
            break
    print("The resulting Array is: " + str(Numbers) + "\n")

# SequenceChecker
def Sequence_Check(InputArray):
    output = (InputArray[len(InputArray)-1]).find(InputArray[len(InputArray)-2]) != -1
    print ("The last value contains the one to last value: " + str(output) + "\n")
    return output

while True:

    print("""\n\n
  __  __       _ _   _ _______          _              ___   ____  
 |  \/  |     | | | (_)__   __|        | |            / _ \ |___ \ 
 | \  / |_   _| | |_ _   | | ___   ___ | |   __   __ | | | |  __) |
 | |\/| | | | | | __| |  | |/ _ \ / _ \| |   \ \ / / | | | | |__ < 
 | |  | | |_| | | |_| |  | | (_) | (_) | |    \ V /  | |_| | ___) |
 |_|  |_|\__,_|_|\__|_|  |_|\___/ \___/|_|     \_(_)  \___(_)____/ 
                                                                   
Please select a tool or EXIT to exit.
""")
    Tools()
    ToolInput = input("\nTool: ")
    if not ToolInput.isnumeric():
        print("Quitting MultiTool v. " + ToolKitVersion)
        exit()


    Tool = int(ToolInput)

    if Tool == 1:
        print("""\n\n
   _____      _ _            _        _____ _               _                          ___  __ 
  / ____|    (_) |          (_)      / ____| |             | |                        / _ \/_ |
 | |     _ __ _| |_ ___ _ __ _  __ _| |    | |__   ___  ___| | _____ _ __    __   __ | | | || |
 | |    | '__| | __/ _ \ '__| |/ _` | |    | '_ \ / _ \/ __| |/ / _ \ '__|   \ \ / / | | | || |
 | |____| |  | | ||  __/ |  | | (_| | |____| | | |  __/ (__|   <  __/ |       \ V /  | |_| || |
  \_____|_|  |_|\__\___|_|  |_|\__,_|\_____|_| |_|\___|\___|_|\_\___|_|        \_(_)  \___(_)_|
\n
""")
        print("Enter a number to check if it meets the criteria, Or enter any letter to quit\n")

        while True:
            inputNumber = input("Enter a number: ")
            if not inputNumber.isnumeric():
                break
            inputNumber = int(inputNumber)
        
            CriteriaChecker_Check(inputNumber)

    elif Tool == 2:
        print("""\n\n
   _____      _ _            _        _____ _               _                          ___   ___  
  / ____|    (_) |          (_)      / ____| |             | |                        / _ \ |__ \ 
 | |     _ __ _| |_ ___ _ __ _  __ _| |    | |__   ___  ___| | _____ _ __    __   __ | | | |   ) |
 | |    | '__| | __/ _ \ '__| |/ _` | |    | '_ \ / _ \/ __| |/ / _ \ '__|   \ \ / / | | | |  / / 
 | |____| |  | | ||  __/ |  | | (_| | |____| | | |  __/ (__|   <  __/ |       \ V /  | |_| | / /_ 
  \_____|_|  |_|\__\___|_|  |_|\__,_|\_____|_| |_|\___|\___|_|\_\___|_|        \_(_)  \___(_)____|
\n\n
""")
        print("Enter a number to check if it meets the criteria, Or enter any letter to quit\n")

        while True:
            inputNumber = input("Enter a number: ")
            if not inputNumber.isnumeric():
                break
    
            inputNumber = int(inputNumber)

            if not (CriteriaChecker_Check(inputNumber)):
                CriteriaChecker_Find(inputNumber)

            print()
    elif Tool == 3:
        print("""\n\n
  _   _                 _                                                        ___  __ 
 | \ | |               | |               /\                                     / _ \/_ |
 |  \| |_   _ _ __ ___ | |__   ___ _ __ /  \   _ __ _ __ __ _ _   _    __   __ | | | || |
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__/ /\ \ | '__| '__/ _` | | | |   \ \ / / | | | || |
 | |\  | |_| | | | | | | |_) |  __/ | / ____ \| |  | | | (_| | |_| |    \ V /  | |_| || |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|/_/    \_\_|  |_|  \__,_|\__, |     \_(_)  \___(_)_|
                                                               __/ |                     
                                                              |___/                      

""")
        print("Enter a number to see a array starting with it, Or enter any letter to quit\n")
        while True:
            inputNumber = input("Enter a number: ")
            if not inputNumber.isnumeric():
                break
            inputNumber = int(inputNumber)
            if inputNumber >= 1:
                NumberArray(inputNumber)
            else:
                print("\033[91mError: It is not possible to have a array starting at " + str(inputNumber) + " containing " + str(inputNumber) + ".\033[0m\nPlease enter another number.\n")
    elif Tool == 4:
        print("""\n\n
   _____                                       _____ _               _                         ___  __ 
  / ____|                                     / ____| |             | |                       / _ \/_ |
 | (___   ___  __ _ _   _  ___ _ __   ___ ___| |    | |__   ___  ___| | _____ _ __   __   __ | | | || |
  \___ \ / _ \/ _` | | | |/ _ \ '_ \ / __/ _ \ |    | '_ \ / _ \/ __| |/ / _ \ '__|  \ \ / / | | | || |
  ____) |  __/ (_| | |_| |  __/ | | | (_|  __/ |____| | | |  __/ (__|   <  __/ |      \ V /  | |_| || |
 |_____/ \___|\__, |\__,_|\___|_| |_|\___\___|\_____|_| |_|\___|\___|_|\_\___|_|       \_(_)  \___(_)_|
                 | |                                                                                   
                 |_|                                                                                   
""")    
        print("Enter an array to check if the last value contains the one to last value, Or EXIT to quit\n")
        while True:
            InputArray = input("Enter a array: ")
            if InputArray.lower() == "exit":
                break
            InputArray = InputArray.replace("[", "").replace("]", "").replace("'", "").split(', ')
            if len(InputArray) <= 1:
                print("\033[91mERROR, The submitted array is invalid/too short.\033[0m\n")
            else:
                Sequence_Check(InputArray)

    else:
        print("\033[91mERROR, Tool not found\033[0m")
    print("Quitting this tool...\n\n\n")