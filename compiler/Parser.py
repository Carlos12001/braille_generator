from sly import Parser
from Lexer import brailleLexer

class brailleParser(Parser):

    debugfile = 'parser.out'

    tokens = brailleLexer.tokens

    #Grammar rules

    def __init__(self):
        self.env = { }

    @_('procedure procedures')
    def procedures(self, p):
        return ('function', p.procedure, p.procedures)

    @_('')
    def procedures(self, p):
        pass

    @_('PROC ID "(" statements ")" ";" ')
    def procedure(self, p):
        return ('procedure', p.ID, p.statements)
    
    @_('statements statement',
       'statements operator')
    def statements(self, p):
        return ('instructions', p.statements, p[1])
    
    @_('statement',
       'operator',
       'condition')
    def statements(self, p):
        return ('instructions', p[0])
    
    @_('')
    def statement(self, p):
        pass
    
    @_('CALL "(" ID ")" ";" ')
    def statement(self, p):
        return ('proc_call', p.ID)
    
    @_('NEW ID "," "(" NTYPE "," NUM ")" ";" ',
       'NEW ID "," "(" BTYPE "," boolean ")" ";" ')
    def statement(self, p):
        return ('new_var', p.ID, p[4], p[6])
    
    @_('VALUES "(" ID "," NUM ")" ";" ',
       'VALUES "(" ID "," boolean ")" ";" ',
       'VALUES "(" ID "," operator ")" ";" ')
    def statement(self, p):
        return ('values', p.ID, p[4])
    
    @_('SIGNAL "(" NUM "," NUM ")" ";" ',
       'SIGNAL "(" ID "," NUM ")" ";" ',
       'SIGNAL "(" operator "," NUM ")" ";" ')
    def statement(self, p):
        return ('signal', p[2], p[4])

    @_('RPT "(" statements BRK ")" ";" ')
    def statement(self, p):
        return ('repeat', p.statements)

    @_('UNT "(" statements ")" condition ";" ')
    def statement(self, p):
        return ('until', p.statements, p.condition)

    @_('WHILE condition "(" statements ")" ";" ')
    def statement(self, p):
        return ('while', p.condition, p.statements)
    
    @_('CASE ID cases ";" ')
    def statement(self, p):
        return ('case', p.ID, p.cases)
    
    @_('PRINT "(" params ")" ";" ')
    def statement(self,p):
        return ('print', p.params)
    
    @_('')
    def params(self, p):
        pass

    @_('param')
    def params(self, p):
        return ('params', p.param)
    
    @_('param "," params')
    def params(self, p):
        return ('params', p.param, p.params)

    @_('ID',
      'NUM')
    def param(self, p):
        return p[0]

    @_('')
    def cases(self, p):
        pass

    @_('case cases ')
    def cases(self, p):
        return ('cases', p.case, p.cases)

    @_('cases case ELSE "(" statements ")" ')
    def cases(self, p):
        return ('cases', p.cases, p.case, p.ELSE, p.statements)
    
    @_('WHEN NUM THEN "(" statements ")" ',
       'WHEN boolean THEN "(" statements ")" ')
    def case(self, p):
        return ('when', p[1], p.statements)
    
    @_('ID operand expr',
       'NUM operand expr',
       'boolean operand expr',)
    def condition(self, p):
        return ('num_cond', p[0], p.operand, p[2])
    
    @_('IT "(" ID ")" ";" ')
    def condition(self, p):
        return ('bool_cond', p.ID)

    @_('ALTER "(" ID "," OP "," NUM ")" ";" ')
    def operator(self, p):
        return ("alter", p.ID, p.OP, p.NUM)
    
    @_('ALTERB "(" ID ")" ";" ')
    def operator(self, p):
        return ("alterb", p.ID)
    
    @_('GT',
       'LT',
       'EQEQ',
       'DIFF',
       'GE',
       'LE')
    def operand(self,p):
        return p[0]
    
    @_('ID',
       'NUM',
       'boolean',
       'statement')
    def expr(self,p):
        return p[0]

    @_('TRUE',
       'FALSE')
    def boolean(self,p):
        return p[0]
    
    
    

if __name__ == '__main__':
    lexer = brailleLexer()
    parser = brailleParser()

    env = {}

    data = '''
//Comentario inicial
Proc @Master
(
Values (@variable1, 1);
PrintValues (@variable1);
);
'''

    result = parser.parse(lexer.tokenize(data))
    print(result)
    
    