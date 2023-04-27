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


def p_stm_semi (p):
    '''stm : exp SEMI
    '''
    pass

def p_stm_while (p):
    '''stm : WHILE exp bodyorstm
    '''
    pass

def p_stm_if (p):
    ''' stm : IF exp bodyorstm 
    '''
    pass

def p_stm_if2 (p):  #PROF ME AJUDAAAAA
    ''' stm :  IF exp bodyorstm ELSE stm 
    '''
    pass
def p_stm_for (p):
    ''' stm : FOR ID IN stm2 body
    '''
    pass


def p_stm_for2 (p):
    ''' stm : FOR ID IN ID body 
    '''
    pass

def p_stm_return (p):
    ''' stm : RETURN exp SEMI
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

def p_exp_assign (p):
    ''' exp : exp EQEQ exp1
            | exp1

    '''
    pass

def p_exp_plus (p):
    '''exp1 : exp1 PLUS exp2
            | exp2
    '''
    pass

def p_exp_minus (p):
    '''exp1 : exp1 MINUS exp2
    '''
    pass

def p_exp_star(p):
    ''' exp2 : exp2 STAR exp3
             | exp3
    '''
    pass

def p_exp_slash(p):
    ''' exp2 : exp2 SLASH exp3
             
    '''
    pass

def p_exp_percent(p):
    ''' exp2 : exp2 PERCENT exp3             
    '''
    pass


def p_exp_caret(p):
    ''' exp3 : exp3 CARET exp4
             | exp4        
    '''
    pass

def p_exp_and (p):
    ''' exp4 : exp4 and exp5
    
    '''
    pass

def p_exp_or (p):
    ''' exp4 : exp4 OR exp5
    
    '''
    pass

def p_exp_oror (p):
    ''' exp4 : exp4 OROR exp5
    
    '''
    pass

def p_exp_andand (p):
    ''' exp4 : exp4 ANDAND exp5
    '''
    pass

def p_exp_not (p):
    ''' exp4 : exp4 NOT exp5
    '''
    pass

def p_exp_ge(p):
    ''' exp4 : exp4 GE exp5      
    '''
    pass

def p_exp_gt(p):
    ''' exp4 : exp4 GT exp5  
    '''
    pass


def p_exp_le(p):
    ''' exp4 : exp4 LE exp5      
    '''
    pass


def p_exp_lt(p):
    ''' exp4 : exp4 LT exp5      
    '''
    pass

def p_exp_eqeq(p):
    ''' exp4 : exp4 EQEQ exp5      
    '''
    pass

def p_exp_eq(p):
    ''' exp4 : exp4 EQ exp5      
    '''
    pass

def p_exp_slasheq(p):
    ''' exp4 : exp4 SLASHEQ exp5      
    '''
    pass

def p_exp_pluseq(p):
    ''' exp4 : exp4 PLUSEQ exp5      
    '''
    pass

def p_exp_stareq(p):
    ''' exp4 : exp4 STAREQ exp5      
    '''
    pass

def p_exp_minuseq(p):
    ''' exp4 : exp4 MINUSEQ exp5      
    '''
    pass

def p_exp_andeq(p):
    ''' exp4 : exp4 ANDEQ exp5      
    '''
    pass


def p_exp_careteq(p):
    ''' exp4 : exp4 CARETEQ exp5      
    '''
    pass

def p_exp_ne(p):
    ''' exp4 : exp4 NE exp5      
    '''
    pass

def p_exp_questionandcolon(p):
    ''' exp5 : exp5 QUESTION exp5 COLON exp6      
    '''
    pass

def p_exp_number(p):
    ''' exp6 : NUMBER     
    '''
    pass

def p_exp_id(p):
    ''' exp6 : ID     
    '''
    pass

def p_exp_assign(p):
    ''' exp6 : assign     
    '''
    pass

def p_exp_call(p):
    ''' exp6 : call     
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


def p_tipo(p):  #PROF ME AJUDAAAAA
    '''tipo : ITT
            | UTT
            | FTT
            | STRING
            | CHAR
    '''
    pass


parser = yacc.yacc()
parser.parse(debug=True)
