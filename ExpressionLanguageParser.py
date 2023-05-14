import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

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


def p_stm_semi(p):
    '''stm : exp SEMI
    '''
    pass


def p_stm_assign(p):
    '''stm : assign SEMI
    '''
    pass


def p_stm_while(p):
    '''stm : WHILE exp bodyorstm
    '''
    pass


def p_stm_if(p):
    ''' stm : IF exp bodyorstm 
    '''
    pass


def p_stm_if2(p):  # PROF ME AJUDAAAAA
    ''' stm :  IF exp bodyorstm ELSE stm 
    '''
    pass


def p_stm_for(p):
    ''' stm : FOR ID IN stm2 body
    '''
    pass


def p_stm_for2(p):
    ''' stm : FOR ID IN ID body 
    '''
    pass


def p_stm_return(p):
    ''' stm : RETURN exp SEMI
    '''
    pass


def p_stm2(p):
    '''stm2 : LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES
            | LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES DOT ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    pass

def p_exp_star(p):
    ''' exp : exp STAR exp1
             | exp1
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.StarExp(p[1], p[3])

def p_exp_slash(p):
    ''' exp : exp SLASH exp1

    '''
    p[0] = sa.SlashExp(p[1], p[3])

def p_exp_percent(p):
    ''' exp : exp PERCENT exp1             
    '''
    p[0] = (p[1], p[3])

def p_exp_plus(p):
    '''exp1 : exp1 PLUS exp2
            | exp2
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.PlusExp(p[1], p[3])


def p_exp_minus(p):
    '''exp1 : exp1 MINUS exp2
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.MinusExp(p[1], p[3])


def p_exp_and(p):
    '''exp2 : exp2 AND exp3
            | exp3            
    '''
    p[0] = sa.AndExp(p[1], p[3])

def p_exp_caret(p):
    ''' exp3 : exp3 CARET exp4
             | exp4       
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.CaretExp(p[1], p[3])

def p_exp_or(p):
    '''exp4 : exp4 OR exp5
            | exp5             
    '''
    p[0] = sa.OrExp(p[1], p[3])

def p_exp_assign(p):
    ''' exp5 : exp5 EQEQ exp6
            | exp6

    '''
    p[0] = sa.AssignExp(p[1], p[3])

def p_exp_ne(p):
    '''exp5 : exp5 NE exp6      
    '''
    p[0] = sa.NeExp(p[1], p[3]) 


def p_exp_lt(p):
    '''exp5 : exp5 LT exp6     
    '''
    p[0] = sa.LtExp(p[1], p[3])


def p_exp_gt(p):
    '''exp5 : exp5 GT exp6     
    '''
    p[0] = sa.GtExp(p[1], p[3])

def p_exp_ge(p):
    ''' exp5 : exp5 GE exp6      
    '''
    p[0] = sa.GeExp(p[1], p[3])

def p_exp_le(p):
    ''' exp5 : exp5 LE exp6      
    '''
    p[0] = sa.LeExp(p[1], p[3])

def p_exp_andand(p):
    '''exp6 : exp6 ANDAND exp7
            | exp7
    '''
    p[0] = sa.AndAndExp(p[1], p[3])

def p_exp_oror(p):
    '''exp7 : exp7 OROR exp8
            | exp8
    '''
    p[0] = sa.OrOrExp(p[1], p[3])


def p_exp_number(p):
    '''exp8 : NUMBER
            
    '''
    p[0] = sa.NumberExp(p[1])


def p_exp_id(p):
    ''' exp8 : ID     
    '''
    p[0] = sa.IdExp(p[1])

def p_exp_call(p):
    ''' exp8 : call     
    '''
    p[0] = (p[1])



# def p_exp_questionandcolon(p):
#     ''' exp8 : exp8 QUESTION exp8 COLON exp9    
#     '''
#     p[0] = (p[1], p[3], p[5])


# def p_exp_assign2(p):
#     ''' exp6 : assign
#     '''
#     p[0] = (p[1])



def p_call(p):
    '''call : ID LEFTPARENTHESES params RIGHTPARENTHESES
            | ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    if len(p) == 5:
        p[0] = sa.CallExp(p[1], p[3])
    else:
        p[0] = sa.CallExp(p[1])


def p_params(p):
    '''params : exp COMMA params 
                | exp
    '''
    if len(p) == 2:
        p[0] = sa.OneParams(p[1]) 
    elif len(p) == 4:
        p[0] = sa.MoreParams(p[1], p[3])
 

def p_assign(p):
    '''assign : ID EQ exp
    '''
    pass


def p_tipo(p):  # PROF ME AJUDAAAAA
    '''tipo : ITT
            | UTT
            | FTT
            | STRING
            | CHAR
    '''
    pass


parser = yacc.yacc()
parser.parse(debug=True)
