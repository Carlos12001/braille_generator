from Lexer import brailleLexer
from Parser import brailleParser

Consolelog = []

def check_first_comment(string):
    if(string.startswith("//")):
        return ""
    else:
        return "Error: Initial comment is missing!"
    
def run(plist):
    print("fuck")

#Parametros: tupla con un procedimiento en solitario
#Retorna: Null si recibe parametro erroneo, instruction_stack_aux(tupla instrucciones, tupla vacia)
def instruction_stack(procedure):
    if(procedure[0] != 'procedure'):
        return None
    else:
        if(len(procedure)>2):
            return instruction_stack_aux(procedure[2], ())
        else:
            return None

#Parametros: tupla arbol con las Instructions de un procedimiento, tupla vacia par almacenar resultado
#Retorna: tupla de las instrucciones o funciones en orden de ejecucion        
def instruction_stack_aux(lst, res):
    if(lst[0] == 'instructions'):
        if(len(lst)==2):
            res += ((instruction_match(lst[1])), )
            return res
        if(len(lst)==3):
            res = instruction_stack_aux(lst[1], res)
            res += (instruction_match(lst[2]), )
            return res
        else:
            print("Error, instructions tiene problemas familiares")
            return None    
    else:
        print("Error, no instructions encontrado")
        return res

#Parametros tupla simple o anidada de una funcion
#Retorna tupla simple de la funcion   
def instruction_match(lst):
    match lst[0]:
        case 'print':
            return print_case(lst, ())
        case 'case':
            return cases_case(lst, ())
        case other:
            return lst

#Parametros: tupla arbol de un print, una tupla vacia para almacenar resultado
#Retorna Tupla simple de la funcion de print
def print_case(lst, res):
    if(lst[0]=='print'):
        res += ((lst[0]), )
        res = print_case(lst[1], res)
        return res 
    else:
        if(len(lst)>2):
            res += ((lst[1]), )
            res = print_case(lst[2], res)
            return res
        else:
            res += ((lst[1]), )
            return res

def cases_case(vanilla_tuple, res):
    if(vanilla_tuple[0] == 'case'):
        res += (vanilla_tuple[0], )
        res += (vanilla_tuple[1], )
        res = cases_case(vanilla_tuple[2], res)
        return res
    if(vanilla_tuple[0] == 'cases'):
        if(len(vanilla_tuple) == 3):
            res = cases_case(vanilla_tuple[1], res)
            res = cases_case(vanilla_tuple[2], res)
            return res
        else:
            res = cases_case(vanilla_tuple[1], res)
            res += (vanilla_tuple[3],)
            res = cases_case(vanilla_tuple[4], res)
            return res
    if(vanilla_tuple[0] == 'when'):
        res += (vanilla_tuple[1], )
        res = cases_case(vanilla_tuple[2], res)
        return res
    if(vanilla_tuple[0] == 'instructions'):
        res += (instruction_match(vanilla_tuple[1]), )
        return res


#Parametros: tupla arbol, nombre de procedimiento a buscar
#Retorna: tupla arbol que unicamente contiene el procedimiento buscado. 
def searchProcedure(lst, procedure_name):
    if lst is None:
        return None
    if lst[0] == 'function' and lst[1][1] == procedure_name:
        return lst[1]
    elif lst[0] == 'function':
        for item in lst[2:]:
            result = searchProcedure(item, procedure_name)
            if result:
                return result
    return None


if __name__ == '__main__':
    lexer = brailleLexer()
    parser = brailleParser()

    env = {}

    data = '''//Comentario inicial
Proc @Master
(
NEW @variable1, (Num, 1);
NEW @variable2, (Bool, True);
Case @variable1
When 1 Then
( Signal(@variale1, 0);)
When 2 Then
( Signal(@variale1, 0);)
Else
( CALL(@pedro););
Repeat
(
 NEW @variable1, (Num, 5);
Signal(1, 1);
Break;
);
);

Proc @Pedro
(
Values (@var, True);
While IsTrue(@variale2);
 ( Signal(@variale2, 1);
// Cambia variable a False
 AlterB (@variable2);
);
PrintValues ("Aqui procedimiento ", @variable1, " pedro");
Until
 (
// Aumenta en 1 a la variable
 Values (@variable1,
 Alter (@variable1,ADD, 1););
 )
 @variable1 > 10;
);
'''
    parsedlist = parser.parse(lexer.tokenize(data))
    #print(parsedlist)
    #print(searchProcedure(parsedlist, "@Master"))
    #print(instruction_stack(searchProcedure(parsedlist, "@Master")))
    print(instruction_match(('case', '@variable1', ('cases', ('when', 1, ('instructions', ('signal', '@variale1', 0))), ('cases', ('when', 2, ('instructions', ('signal', '@variale1', 0))), None, 'Else', ('instructions', ('proc_call', '@pedro')))))))    
    
    #print(check_first_comment(data))
