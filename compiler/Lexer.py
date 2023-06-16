from sly import Lexer

class brailleLexer(Lexer):

    #Set of tokens
    tokens = { ID, NUM, OP, PROC,
               TRUE, FALSE, VALUES, ALTER,
               NEW, NTYPE, BTYPE, CALL,
               ALTERB, SIGNAL, VS, GT, LT,
               EQEQ, DIFF, GE, LE, IT,
               RPT, BRK, UNT, WHILE,
               CASE, WHEN, THEN, ELSE,
               PRINT, STRING}

    #Ignore spaces
    ignore ='\t '

    #Symbols
    literals = { '(', ')', ',', ';' }

    # Regular expressions for tokens
    TRUE = r'True'
    FALSE = r'False'
    NTYPE = r'Num'
    BTYPE = r'Bool'
    OP = r'ADD|SUB|MUL|DIV'
    DIFF = r'<>'
    GE = r'>='
    LE = r'<='
    GT = r'>'
    LT = r'<'
    EQEQ = r'=='
    PRINT = r'PrintValues'

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t
    
    @_(r'"([^"\\]|\\.)*"')
    def STRING(self, t):
        t.value = t.value[1:-1]  # This removes the double quote around
        return t
    
    #Identifiers and keywords
    ID = r'@[a-zA-Z0-9?_]{1,11}'
    PROC = r'Proc'
    VALUES = r'Values'
    NEW = r'NEW'
    CALL = r'CALL'
    ALTERB = r'AlterB'
    ALTER = r'Alter'
    SIGNAL = r'Signal'
    VS = r'ViewSignal'
    IT = r'IsTrue'
    RPT = r'Repeat'
    BRK = r'Break;'
    UNT = r'Until'
    WHILE = r'While'
    CASE = r'Case'
    WHEN = r'When'
    THEN = r'Then'
    ELSE = r'Else'

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
Values (@variable1, 1);
PrintValues (@variable1);
);
'''
    lexer = brailleLexer()
    for tok in lexer.tokenize(data):
        print(tok)