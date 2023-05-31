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
Proc @Pedro
(
PrintValues ("ayuda", "por favor");
);
Proc @Master
(
NEW @Variable1, (Num, 1);
Values (@variable1, 5);
PrintValues ("Hola", @variable1, "adios compi 
2023");
PrintValues ("ayuda", "por favor");
);
Proc @Juan
(
PrintValues ("Adios");
);
'''
    parsedlist = parser.parse(lexer.tokenize(data))
    #print(parsedlist)
    #run(parsedlist)
    print(searchProcedure(parsedlist, "@Master"))
    #print(check_first_comment(data))
