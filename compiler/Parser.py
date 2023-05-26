from sly import Parser
from Lexer import brailleLexer

class brailleParser(Parser):

    tokens = brailleLexer.tokens

    #Grammar rules

    def __init__(self):
        self.env = { }

    @_('procedure statements')
    def procedures(self, p):
        return p.procedure + p.statements

    @_('statements procedure')
    def statements(self, p):
        return p.statements + p.procedure

    @_('PROC ID "(" statements ")" ";" ')
    def procedure(self, p):
        return ('procedure', p.ID, p.statements)
    
    @_('statements statement')
    def statements(self, p):
        return ('proc_body', p.statements, p.statement)
    
    @_('statement')
    def statements(self, p):
        return ('proc_body', p.statement)
    
    @_('')
    def statement(self, p):
        pass
    
    @_('CALL "(" ID ")" ";" ')
    def statement(self, p):
        return ('proc_call', p.ID)
    
    @_('NEW ID "," "(" NTYPE "," NUM ")" ";" ',
       'NEW ID "," "(" BTYPE "," TRUE ")" ";" ',
       'NEW ID "," "(" BTYPE "," FALSE ")" ";" ')
    def statement(self, p):
        return ('new_var', p.ID, p[4], p[6])
    
if __name__ == '__main__':
    lexer = brailleLexer()
    parser = brailleParser()

    env = {}

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

Proc @adios
(

);
'''

    result = parser.parse(lexer.tokenize(data))
    print(result)
    
    