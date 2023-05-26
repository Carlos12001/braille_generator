from sly import Lexer

class brailleLexer(Lexer):

    #Set of tokens
    tokens = { ID, NUM, PROC,
               TRUE, FALSE, 
               NEW, NTYPE, BTYPE, CALL}

    #Ignore spaces
    ignore ='\t '

    #Symbols
    literals = { '(', ')', ',', ';' }

    # Regular expressions for tokens
    TRUE = r'True'
    FALSE = r'False'
    NTYPE = r'Num'
    BTYPE = r'Bool'

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t
    
    #Identifiers and keywords
    ID = r'@[a-zA-Z0-9?_]{1,11}'
    PROC = r'Proc'
    NEW = r'New'
    CALL = r'CALL'

    ignore_comment = r'//.*'

    #Line tracking
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Undefined character %r in line %d' % (t.value[0], self.lineno))
        self.index += 1

if __name__ == '__main__':
    data = '''
//Comentario inicial
Proc @Master
(
CALL(@hola);
);

Proc @hola
(
New @variable1, (Num, 5);
);
'''
    lexer = brailleLexer()
    for tok in lexer.tokenize(data):
        print(tok)