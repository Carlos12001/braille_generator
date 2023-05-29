from Lexer import brailleLexer
from Parser import brailleParser

def check_first_comment(string):
    if(string.startswith("//")):
        return ""
    else:
        return "Error: Initial comment is missing!"
    

if __name__ == '__main__':
    lexer = brailleLexer()
    parser = brailleParser()

    env = {}

    data = '''//Comentario inicial
Proc @Master
(

)
'''
    print(check_first_comment(data))
