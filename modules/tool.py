import modules.tools

def read():
    with open('tools.txt', 'r') as toolFile:
        toolList = ''.join(toolFile.readlines())
        return toolList

"""
Get name, version, datatype or action by entering a tool number
toolNumber=The tool number
type="name" for tool name
type="version" for tool version
type="datatype" for tool datatype
type="all" for all of the above. (standard)
"""
def get(toolNumber, type="all"):
    match type:
        case "name":
            type = 0
        case "version":
            type = 1
        case "datatype":
            type = 2
        case "action":
            type = 3
        case "all":
            toolList = read().split('\n')
            tool = toolList[toolNumber-1].split('|')
            return tool

    toolList = read().split('\n')
    tool = "".join(filter(str.isalpha, toolList[toolNumber-1].split('|')[type].lower()))
    return tool

def run(toolNumber, input):
    match get(toolNumber, "action"):
        case "criteriacheck":
            return modules.tools.criteriachecker.check(input)

        case "criteriafind":
            success = modules.tools.criteriachecker.check(input)
            if not success:
                return modules.tools.criteriachecker.find(input)
            return success
        
        case "numberarray":
            return modules.tools.numberarray.get(input)

        case "sequencecheck":
            return modules.tools.sequencechecker.get(input)

        case "samedistance":
            return modules.tools.samedistancechecker.get(input)

        case "closebrackets":
            return modules.tools.brackets.close(input)
        
        case "startswith":
            return modules.tools.startswith.get(input)

        case "longestwords":
            return modules.tools.longestwords.get(input)

        case "multiplynumbers":
            return modules.tools.multiplynumbers.odd(input)

        case "convertgrade":
            return modules.tools.grades.letter(input)