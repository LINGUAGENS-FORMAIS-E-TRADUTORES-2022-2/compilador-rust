import ply.yacc as yacc
from ExpressionLanguageLex import *


def p_program(p):
    '''program : funcdecl
                | funcdecl program
                | declvar 
                | declvar program
    '''
    pass


def p_declvar(p):
    '''declvar : LET assign SEMI 
                | LET MUT assign SEMI
    '''
    pass


def p_funcdecl(p):
    '''funcdecl : signature body
    '''
    pass


def p_signature(p):
    '''signature : FN ID LEFTPARENTHESES sigparams RIGHTPARENTHESES
                | FN ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    pass


def p_sigparams(p):
    '''sigparams : ID COLON tipo
                | ID COLON tipo COMMA sigparams
    '''
    pass


def p_stms(p):
    '''stms : stm  
            | stm  stms
    '''
    pass


def p_body(p):
    '''body : LEFTBRACKET stms RIGHTBRACKET
    '''
    pass


def p_bodyorstm(p):
    '''bodyorstm : stm 
                | body
    '''
    pass


def p_stm(p):
    '''stm : exp SEMI 
            | WHILE exp bodyorstm
            | IF exp bodyorstm 
            | IF exp bodyorstm ELSE stm 
            | FOR ID IN stm2 body 
            | FOR ID IN ID body 
            | RETURN exp SEMI
    '''
    pass


def p_stm2(p):
    '''stm2 : LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES
            | LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES DOT ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    pass


precedence = (
    (
        'left',
        'PLUSEQ',
        'MINUSEQ',
        'STAREQ',
        'SLASHEQ',
        'PERCENTEQ',
        'CARETEQ',
        'ANDEQ',
        'OREQ',
        'SHLEQ',
        'SHREQ',
        'EQ',
        'EQEQ',
        'NE',
        'GT',
        'LT',
        'GE',
        'LE',
    ),
    ('left', 'PLUS', 'MINUS', 'SHL', 'SHR'),
    ('left', 'NOT', 'AND', 'OR', 'ANDAND', 'OROR'),
    ('left', 'STAR', 'SLASH', 'PERCENT'),
    ('left', 'CARET')
)


def p_exp(p):
    '''exp : exp PLUS exp
            | exp MINUS exp
            | exp STAR exp
            | exp CARET exp
            | exp SLASH exp
            | exp PERCENT exp
            | exp AND exp
            | exp OR exp
            | exp GE exp
            | exp GT exp
            | exp LE exp
            | exp LT exp
            | exp AS exp
            | exp IS exp
            | exp ISEXCLAMATION exp
            | exp EQEQ exp
            | exp NE exp
            | exp ANDAND exp
            | exp OROR exp
            | exp QUESTIONQUESTION exp
            | exp QUESTION exp COLON exp
            | exp EQ exp
            | exp STAREQ exp
            | exp SLASHEQ exp
            | exp PLUSEQ exp
            | exp MINUSEQ exp
            | exp ANDEQ exp
            | exp CARETEQ exp
            | call
            | assign
            | NUMBER
            | ID
    '''
    pass


def p_call(p):
    '''call : ID LEFTPARENTHESES params RIGHTPARENTHESES
            | ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    pass


def p_params(p):
    '''params : exp COMMA params 
                | exp
    '''
    pass


def p_assign(p):
    '''assign : ID EQ exp
    '''
    pass


def p_tipo(p):
    '''tipo : ITT
            | UTT
            | FTT
            | STRING
            | CHAR
    '''
    pass


parser = yacc.yacc()
parser.parse(debug=True)
