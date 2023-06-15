from compiler import *

def brailleRun(lst, instr, glb , lc, proc):
    for i in range(len(instr)):

        if instr[i][0] == 'proc_call':
            if searchProcedure(parsedlist, instr[i][1]):
                called = instruction_stack(searchProcedure(parsedlist, instr[i][1]))
                brailleRun(lst, called ,glb , lc, "L")
                lc.clear()
            else:
                print("Error: procedure '" +instr[i][1]+ "' doesnt exist!")


        if instr[i][0] == 'new_var':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                print("Error: variable '" +instr[i][1]+ "' already exists!")
                break
            else:
                if proc == "G":
                    glb.append([instr[i][1],instr[i][2],instr[i][3]])
                else:
                    lc.append([instr[i][1],instr[i][2],instr[i][3]])


        if instr[i][0] == 'alter':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                if isinstance(varCheck(glb, instr[i][1]), int):
                    if instr[i][2] == 'ADD':
                        varAlter(glb, instr[i][1], varCheck(glb, instr[i][1]) + instr[i][3])
                    elif instr[i][2] == 'SUB':
                        varAlter(glb, instr[i][1], varCheck(glb, instr[i][1]) - instr[i][3])
                    elif instr[i][2] == 'MUL':
                        varAlter(glb, instr[i][1], varCheck(glb, instr[i][1]) * instr[i][3])
                    elif instr[i][2] == 'DIV':
                        varAlter(glb, instr[i][1], varCheck(glb, instr[i][1]) / instr[i][3])
                elif isinstance(varCheck(lc, instr[i][1]), int):
                    if instr[i][2] == 'ADD':
                        varAlter(glb, instr[i][1], varCheck(lc, instr[i][1]) + instr[i][3])
                    elif instr[i][2] == 'SUB':
                        varAlter(glb, instr[i][1], varCheck(lc, instr[i][1]) - instr[i][3])
                    elif instr[i][2] == 'MUL':
                        varAlter(glb, instr[i][1], varCheck(lc, instr[i][1]) * instr[i][3])
                    elif instr[i][2] == 'DIV':
                        varAlter(glb, instr[i][1], varCheck(lc, instr[i][1]) / instr[i][3])
                else:
                    print("Error: variable '" +instr[i][1]+ "' is not a number!")
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break

        if instr[i][0] == 'signal':
            if isinstance(instr[i][1], str):
                if varExists(glb, instr[i][1]):
                    if isinstance(varCheck(glb, instr[i][1]), int):
                        varValue = varCheck(glb, instr[i][1])
                        print("pos", varValue, "state",instr[i][2])
                    else:
                        print("Error: variable '" +instr[i][1]+ "' is not a number!")
                        break
                elif varExists(lc, instr[i][1]):
                    if isinstance(varCheck(lc, instr[i][1]), int):
                        varValue = varCheck(lc, instr[i][1])
                        print("pos", varValue, "state",instr[i][2])
                    else:
                        print("Error: variable '" +instr[i][1]+ "' is not a number!")
                        break
                else: 
                    print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                    break
            
            elif isinstance(instr[i][1], tuple):
                brailleRun(lst, (instr[i][1],) ,glb , lc, "G")
                if varExists(glb, instr[i][1][1]):
                    varValue = varCheck(glb, instr[i][1][1])
                    print("pos", varValue, "state",instr[i][2])
                else:
                    varValue = varCheck(lc, instr[i][1][1])
                    print("pos", varValue, "state",instr[i][2])
                
            else:
                print("pos",instr[i][1],"state", instr[i][2])

    
def varExists(vars, vName):
    if len(vars) == 0:
        return False
    for i in range(len(vars)):
        if vars[i][0] == vName:
            return True
    else:
        return False
    
def varCheck(vars, vName):
    for i in range(len(vars)):
        if vars[i][0] == vName:
                return vars[i][2]

def varAlter(vars, vName, nValue):
    for i in range(len(vars)):
        if vars[i][0] == vName:
                vars[i][2] = nValue

lexer = brailleLexer()
parser = brailleParser()

data = '''//Comentario inicial
Proc @Master
(
NEW @variable1, (Num, 5);
NEW @variable5, (Num, 5);

Signal(Alter (@variable1, ADD, 1);, 0);
Signal(@variable5, 1);
);
'''
parsedlist = parser.parse(lexer.tokenize(data))

#print(instruction_stack(searchProcedure(parsedlist, "@Master")))


if searchProcedure(parsedlist, "@Master"):
        start = instruction_stack(searchProcedure(parsedlist, "@Master"))
        brailleRun(parsedlist, start ,[], [], "G")
else:
        print("Error: procedure @Master is missing!")

#print(searchProcedure(parsedlist, "@Master"))

