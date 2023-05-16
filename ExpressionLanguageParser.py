import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                | declvar 
                | declvar program
    '''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_DecDeclvar(p):
    '''declvar : LET assign SEMI 
                | LET MUT assign SEMI
    '''
    if len(p) == 4:
        p[0] = sa.DecDeclvar(p[2])
    elif len(p) == 5:
        p[0] = sa.DecDeclvar(p[3])



def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.FuncDeclConcrete(p[1], p[2])


def p_signature(p):
    '''signature : FN ID LEFTPARENTHESES sigparams RIGHTPARENTHESES
                | FN ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    if isinstance(p[4], sa.SigParams):
        p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
    else:
        p[0] = sa.SignatureConcrete(p[1], p[2], [])


def p_sigparams(p):
    '''sigparams : ID COLON tipo
                | ID COLON tipo COMMA sigparams
    '''
    if len(p) == 4:
        p[0] = sa.SinglParams([(p[1], p[3])])
           
    else:
         p[0] = sa.CompoundParams(p[1], p[3], p[5])




def p_stms(p):
    '''stms : stm  
            | stm  stms
    '''
    if (len(p) == 2):
        p[0] = sa.SingleStm(p[1])
    else:
        p[0] = sa.CompoundStm(p[1], p[2])

def p_body(p):
    '''body : LEFTBRACKET stms RIGHTBRACKET
    '''
    p[0] = sa.BodyStm(p[1])


def p_bodyorstm(p):
    '''bodyorstm : stm 
                | body

    '''
    p[0] = sa.BodyorStm(p[1])


def p_stm_semi(p):
    '''stm : exp SEMI
    '''
    p[0] = sa.SemiStm(p[1])


def p_stm_assign(p):
    '''stm : assign SEMI
    '''
    p[0] = sa.AssignStm(p[1])


def p_stm_while(p):
    '''stm : WHILE exp bodyorstm
    '''
    p[0] = sa.WhileStm(p[2], p[3])


def p_stm_if(p):
    ''' stm : IF exp bodyorstm 
    '''
    p[0] = sa.IfStm(p[2], p[3])


def p_stm_if2(p):  # PROF ME AJUDAAAAA
    ''' stm :  IF exp bodyorstm ELSE stm 
    '''
    p[0] = sa.IfStm(p[2], p[3], p[5])


def p_stm_for(p):
    ''' stm : FOR ID IN stm2 body
    '''
    p[0] = sa.ForStm(p[4], p[5])


def p_stm_for2(p):
    ''' stm : FOR ID IN ID body 
    '''
    p[0] = sa.For2Stm( p[5])


def p_stm_return(p):
    ''' stm : RETURN exp SEMI
    '''
    p[0] = sa.ReturnStm( p[2])


def p_stm2(p):
    '''stm2 : LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES
            | LEFTPARENTHESES exp DOTDOT exp RIGHTPARENTHESES DOT ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    p[0] = sa.Stm2Stm(p[1], p[3])

def p_exp_star(p):
    ''' exp : exp STAR exp1
             | exp1
    '''
    if len(p) == 2:
        p[0] = sa.StarExp(p[1], p[3])
    else:
        p[0] = p[1]
        

def p_exp_slash(p):
    ''' exp : exp SLASH exp1

    '''
    p[0] = sa.SlashExp(p[1], p[3])

def p_exp_percent(p):
    ''' exp : exp PERCENT exp1             
    '''
    p[0] = sa.PercentExp(p[1], p[3])

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
        p[0] = sa.CallParams(p[1], p[3])
    else:
        p[0] = sa.CallParams(p[1])


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
    p[0] = sa.EqExp(p[1], p[3])
    


def p_tipo(p):  # PROF ME AJUDAAAAA
    '''tipo : ITT
            | UTT
            | FTT
            | STRING
            | CHAR
    '''
    if p[1] == 'ITT':
        p[0] = sa.IntType()
    elif p[1] == 'UTT':
        p[0] = sa.UIntType()
    elif p[1] == 'FTT':
        p[0] = sa.FloatType()
    elif p[1] == 'STRING':
        p[0] = sa.StringType()
    elif p[1] == 'CHAR':
        p[0] = sa.CharType()


parser = yacc.yacc()
parser.parse(debug=True)
