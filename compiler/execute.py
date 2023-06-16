from compiler import *
import contextlib
import io


def brailleRun(lst, instr, glb , lc, proc):
    for i in range(len(instr)):

        if instr[i][0] == 'proc_call':
            if searchProcedure(parsedlist, instr[i][1]):
                called = instruction_stack(searchProcedure(parsedlist, instr[i][1]))
                brailleRun(lst, called ,glb , lc, "L")
                lc.clear()
            else:
                print("Error: procedure '" +instr[i][1]+ "' doesnt exist!")


        elif instr[i][0] == 'new_var':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                print("Error: variable '" +instr[i][1]+ "' already exists!")
                break
            else:
                if proc == "G":
                    glb.append([instr[i][1],instr[i][2],instr[i][3]])
                else:
                    lc.append([instr[i][1],instr[i][2],instr[i][3]])


        elif instr[i][0] == 'values':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                en = varList(glb, lc, instr[i][1])
                if isinstance(instr[i][2], int) and isinstance(varCheck(en, instr[i][1]), int) or isinstance(instr[i][2], str) and isinstance(varCheck(en, instr[i][1]), str):
                    varAlter(en, instr[i][1], instr[i][2])
                elif isinstance(instr[i][2], tuple):
                    brailleRun(lst, (instr[i][2],) ,glb , lc, proc)
                    en2 = varList(glb, lc, instr[i][2][1])
                    if isinstance(varCheck(en2, instr[i][2][1]), int) and isinstance(varCheck(en, instr[i][1]), int) or isinstance(varCheck(en2, instr[i][2][1]), str) and isinstance(varCheck(en, instr[i][1]), str):
                        varAlter(en, instr[i][1], varCheck(en2, instr[i][2][1]))
                    else:
                        print("Error: value doesnt match'" +instr[i][1]+ "' type!")
                else:
                    print("Error: value doesnt match'" +instr[i][1]+ "' type!")
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break


        elif instr[i][0] == 'alter':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                en = varList(glb, lc, instr[i][1])
                if isinstance(varCheck(en, instr[i][1]), int):
                    if instr[i][2] == 'ADD':
                        varAlter(en, instr[i][1], varCheck(en, instr[i][1]) + instr[i][3])
                    elif instr[i][2] == 'SUB':
                        varAlter(en, instr[i][1], varCheck(en, instr[i][1]) - instr[i][3])
                    elif instr[i][2] == 'MUL':
                        varAlter(en, instr[i][1], varCheck(en, instr[i][1]) * instr[i][3])
                    elif instr[i][2] == 'DIV':
                        varAlter(en, instr[i][1], varCheck(en, int(instr[i][1]) / instr[i][3]))
                else:
                    print("Error: variable '" +instr[i][1]+ "' is not a number!")
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break


        elif instr[i][0] == 'alterb':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                en = varList(glb, lc, instr[i][1])
                if isinstance(varCheck(en, instr[i][1]), str):
                    if varCheck(en, instr[i][1]) == 'True':
                        varAlter(en, instr[i][1], 'False')
                    else:
                        varAlter(en, instr[i][1], 'True')
                else:
                    print("Error: variable '" +instr[i][1]+ "' is not a boolean!")
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break



        elif instr[i][0] == 'signal':
            if isinstance(instr[i][1], str):
                if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                    en = varList(glb, lc, instr[i][1])
                    if isinstance(varCheck(en, instr[i][1]), int):
                        if varCheck(en, instr[i][1]) >= 0 and varCheck(en, instr[i][1]) <= 11:
                            if instr[i][2] == 0 or instr[i][2] == 1:
                                varValue = varCheck(en, instr[i][1])
                                print("pos", varValue, "state",instr[i][2])
                            else:
                                print("Error: state '" +instr[i][2]+ "' is not possible!")
                        else:
                            print("Error: position '" +instr[i][1]+ "' is out of range!")
                    else:
                        print("Error: variable '" +instr[i][1]+ "' is not a number!")
                        break
                else: 
                    print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                    break
            
            elif isinstance(instr[i][1], tuple):
                brailleRun(lst, (instr[i][1],) ,glb , lc, proc)
                if varExists(glb, instr[i][1][1]) or varExists(lc, instr[i][1][1]):
                    en = varList(glb, lc, instr[i][1][1])
                    if varCheck(en, instr[i][1][1]) >= 0 and varCheck(en, instr[i][1][1]) <= 11:
                        if instr[i][2] == 0 or instr[i][2] == 1:
                            varValue = varCheck(en, instr[i][1][1])
                            print("pos", varValue, "state",instr[i][2])
                        else:
                            print("Error: state '" +instr[i][2]+ "' is not possible!")
                    else:
                        print("Error: position '" +instr[i][1][1]+ "' is out of range!")
                else:
                    print("Error: variable '" +instr[i][1][1]+ "' doesnt exist!")
                    break
                
            else:
                if instr[i][1] >= 0 and instr[i][1] <= 11:
                    if instr[i][2] == 0 or instr[i][2] == 1:
                        print("pos",instr[i][1],"state", instr[i][2])
                    else:
                        print("Error: state '" +str(instr[i][2])+ "' is not possible!")
                else:
                    print("Error: position '" +str(instr[i][1])+ "' is out of range!")
        

        elif instr[i][0] == 'num_cond':
            if isinstance(instr[i][1], str):
                if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                    en = varList(glb, lc, instr[i][1])
                    if isinstance(varCheck(en, instr[i][1]), int):
                        if isinstance(instr[i][3], int) or isinstance(instr[i][3], bool):
                            if instr[i][2] == '>':
                                return varCheck(en, instr[i][1]) > instr[i][3]
                            elif instr[i][2] == '<':
                                return varCheck(en, instr[i][1]) < instr[i][3]
                            elif instr[i][2] == '==':
                                return varCheck(en, instr[i][1]) == instr[i][3]
                            elif instr[i][2] == '<>':
                                return varCheck(en, instr[i][1]) != instr[i][3]
                            elif instr[i][2] == '>=':
                                return varCheck(en, instr[i][1]) >= instr[i][3]
                            elif instr[i][2] == '<=':
                                return varCheck(en, instr[i][1]) <= instr[i][3]
                        if isinstance(instr[i][3], str):
                            if varExists(glb, instr[i][3]) or varExists(lc, instr[i][3]):
                                en2 = varList(glb, lc, instr[i][3])
                                if instr[i][2] == '>':
                                    return varCheck(en, instr[i][1]) > varCheck(en2, instr[i][3])
                                elif instr[i][2] == '<':
                                    return varCheck(en, instr[i][1]) < varCheck(en2, instr[i][3])
                                elif instr[i][2] == '==':
                                    return varCheck(en, instr[i][1]) == varCheck(en2, instr[i][3])
                                elif instr[i][2] == '<>':
                                    return varCheck(en, instr[i][1]) != varCheck(en2, instr[i][3])
                                elif instr[i][2] == '>=':
                                    return varCheck(en, instr[i][1]) >= varCheck(en2, instr[i][3])
                                elif instr[i][2] == '<=':
                                    return varCheck(en, instr[i][1]) <= varCheck(en2, instr[i][3])
                            else:
                                print("Error: variable '" +instr[i][3]+ "' doesnt exist!")
                                break
                    else:
                        print("Error: variable '" +instr[i][1]+ "' is not a number!")
                else:
                    print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                    break
            else:
                print("Error: first operand '" +instr[i][1]+ "' is not a variable")
                break
        

        elif instr[i][0] == 'bool_cond':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                en = varList(glb, lc, instr[i][1])
                if isinstance(varCheck(en, instr[i][1]), str):
                    if varCheck(en, instr[i][1]) == 'True':
                        return True
                    else:
                        return False
                else:
                    print("Error: variable '" +instr[i][1]+ "' is not boolean!")
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break
        

        elif instr[i][0] == 'repeat':
            for r in range(1, len(instr[i])):
                brailleRun(lst, (instr[i][r],) ,glb , lc, proc)
        
        
        elif instr[i][0] == 'until':
            for u in range(2, len(instr[i])):
                brailleRun(lst, (instr[i][u],) ,glb , lc, proc)
            if brailleRun(lst, (instr[i][1],) ,glb , lc, proc):
                i += 1 
            else:
                brailleRun(lst, (instr[i],) ,glb , lc, proc)

        
        elif instr[i][0] == 'while':
            if brailleRun(lst, (instr[i][1],) ,glb , lc, proc):
                for u in range(2, len(instr[i])):
                    brailleRun(lst, (instr[i][u],) ,glb , lc, proc)
                brailleRun(lst, (instr[i],) ,glb , lc, proc)
            else:
                i += 1
        

        elif instr[i][0] == 'case':
            if varExists(glb, instr[i][1]) or varExists(lc, instr[i][1]):
                en = varList(glb, lc, instr[i][1])
                comp = instr[i][2]
                c = 3
                found = False
                while c < len(instr[i]):
                    if isinstance(instr[i][c], tuple) and varCheck(en, instr[i][1]) == comp or comp == 'Else' and not(found):
                        brailleRun(lst, (instr[i][c],) ,glb , lc, proc)
                        c += 1
                        found = True
                    elif comp == 'Else' and found:
                        i += 1
                    else:
                        comp = instr[i][c]
                        c += 1
            else:
                print("Error: variable '" +instr[i][1]+ "' doesnt exist!")
                break

        
        elif instr[i][0] == 'print':
            output = ''
            p = 1
            while p < len(instr[i]):
                if instr[i][p].startswith('@'):
                    if varExists(glb, instr[i][p]) or varExists(lc, instr[i][p]):
                        en = varList(glb, lc, instr[i][p])
                        output+= str(varCheck(en, instr[i][p]))
                    else:
                        print("Error: variable '" +instr[i][p]+ "' doesnt exist!")
                        break
                    p += 1
                else:
                    output += instr[i][p]
                    p += 1
            print(output)






    
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


def varList(glo, lo, vName):
    if varExists(glo, vName):
        return glo
    else:
        return lo

lexer = brailleLexer()
parser = brailleParser()

data = '''//Comentario inicial
Proc @Master
(
NEW @variable1, (Num, 20);
Case @variable1
When 1 Then
( PrintValues ("Aqui procedimiento ", @variable1, " master");)
When 2 Then
( Signal(@variable1, 1);)
Else
( CALL(@Pedro););

 
  Signal(10, 0);
);

Proc @Pedro
(
NEW @variable2, (Num, 1);
Values (@variable1, Alter (@variable2,ADD, 2););
PrintValues ("Aqui procedimiento ", @variable1, " PEDRO");
);
'''
parsedlist = parser.parse(lexer.tokenize(data))


#print(instruction_stack(searchProcedure(parsedlist, "@Master")))
def run(bltext):
    console = io.StringIO()
    with contextlib.redirect_stderr(console):
        with contextlib.redirect_stdout(console): #Esto captura todos los prints
            parsedlist = parser.parse(lexer.tokenize(bltext))
            if check_first_comment(bltext):
                if searchProcedure(parsedlist, "@Master"):
                    start = instruction_stack(searchProcedure(parsedlist, "@Master"))
                    brailleRun(parsedlist, start ,[], [], "G")
                else:
                    print("Warning: Master procedure could be missing")
            else:
                print("Error: Initial comment is missing!")

    return console.getvalue()


def comp(bltext):
    console = io.StringIO()
    with contextlib.redirect_stderr(console):
        with contextlib.redirect_stdout(console): #Esto captura todos los prints
            parsedlist = parser.parse(lexer.tokenize(bltext))
            if check_first_comment(bltext):
                if searchProcedure(parsedlist, "@Master"):
                    start = instruction_stack(searchProcedure(parsedlist, "@Master"))
                    brailleRun(parsedlist, start ,[], [], "G")
                else:
                    print("Warning: Master procedure could be missing")
            else:
                print("Error: Initial comment is missing!")

    return console.getvalue()


'''
print("banana")

def r_file(txt):
    with contextlib.redirect_stdout(console):
        execute(txt)

r_file(data)
print(console.getvalue())


if check_first_comment(data):
    if searchProcedure(parsedlist, "@Master"):
        start = instruction_stack(searchProcedure(parsedlist, "@Master"))
        brailleRun(parsedlist, start ,[], [], "G")
    else:
        print("Error: procedure @Master is missing!")
else:
    print("Error: Initial comment is missing!")
'''

#print(searchProcedure(parsedlist, "@Master"))

