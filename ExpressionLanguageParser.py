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


# precedence = (
#     (
#         'left',
#         'PLUSEQ',
#         'MINUSEQ',
#         'STAREQ',
#         'SLASHEQ',
#         'PERCENTEQ',
#         'CARETEQ',
#         'ANDEQ',
#         'OREQ',
#         'SHLEQ',
#         'SHREQ',
#         'EQ',
#         'EQEQ',
#         'NE',
#         'GT',
#         'LT',
#         'GE',
#         'LE',
#     ),
#     ('left', 'PLUS', 'MINUS', 'SHL', 'SHR'),
#     ('left', 'NOT', 'AND', 'OR', 'ANDAND', 'OROR'),
#     ('left', 'STAR', 'SLASH', 'PERCENT'),
#     ('left', 'CARET')
# )


def p_exp_assign(p):
    ''' exp : exp EQEQ exp1
            | exp1

    '''
    pass


def p_exp_plus(p):
    '''exp1 : exp1 PLUS exp2
            | exp2
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_exp_minus(p):
    '''exp1 : exp1 MINUS exp2
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_exp_star(p):
    ''' exp2 : exp2 STAR exp3
             | exp3
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_exp_slash(p):
    ''' exp2 : exp2 SLASH exp3

    '''
    p[0] = (p[1], p[3])


def p_exp_percent(p):
    ''' exp2 : exp2 PERCENT exp3             
    '''
    p[0] = (p[1], p[3])


def p_exp_caret(p):
    ''' exp3 : exp3 CARET exp4
             | exp4        
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_exp_exp4_to_exp5(p):
    ''' exp4 : exp5
    '''


def p_exp_and(p):
    ''' exp4 : exp4 AND exp5

    '''
    p[0] = (p[1], p[3])


def p_exp_or(p):
    ''' exp4 : exp4 OR exp5

    '''
    p[0] = (p[1], p[3])


def p_exp_oror(p):
    ''' exp4 : exp4 OROR exp5
    '''
    pass


def p_exp_andand(p):
    ''' exp4 : exp4 ANDAND exp5
    '''
    pass


def p_exp_not(p):
    ''' exp4 : NOT exp5
    '''
    p[0] = (p[1], p[3])


def p_exp_ge(p):
    ''' exp4 : exp4 GE exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_gt(p):
    ''' exp4 : exp4 GT exp5  
    '''
    p[0] = (p[1], p[3])


def p_exp_le(p):
    ''' exp4 : exp4 LE exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_lt(p):
    ''' exp4 : exp4 LT exp5      
    '''
    p[0] = (p[1], p[3])


# def p_exp_eqeq(p):
#     ''' exp4 : exp4 EQEQ exp5
#     '''
#     pass


# def p_exp_eq(p):
#     ''' exp4 : exp4 EQ exp5
#     '''
#     p[0] = (p[1], p[3])


def p_exp_slasheq(p):
    ''' exp4 : exp4 SLASHEQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_pluseq(p):
    ''' exp4 : exp4 PLUSEQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_stareq(p):
    ''' exp4 : exp4 STAREQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_minuseq(p):
    ''' exp4 : exp4 MINUSEQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_andeq(p):
    ''' exp4 : exp4 ANDEQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_careteq(p):
    ''' exp4 : exp4 CARETEQ exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_ne(p):
    ''' exp4 : exp4 NE exp5      
    '''
    p[0] = (p[1], p[3])


def p_exp_questionandcolon(p):
    ''' exp5 : exp5 QUESTION exp5 COLON exp6      
    '''
    p[0] = (p[1], p[3], p[5])


def p_exp_tirarecursao(p):
    '''
        exp5 : exp6
    '''


def p_exp_number(p):
    ''' exp6 : NUMBER     
    '''
    p[0] = (p[1])


def p_exp_id(p):
    ''' exp6 : ID     
    '''
    p[0] = (p[1])


# def p_exp_assign2(p):
#     ''' exp6 : assign
#     '''
#     p[0] = (p[1])


def p_exp_call(p):
    ''' exp6 : call     
    '''
    p[0] = (p[1])


def p_call(p):
    '''call : ID LEFTPARENTHESES params RIGHTPARENTHESES
            | ID LEFTPARENTHESES RIGHTPARENTHESES
    '''
    if len(p) == 5:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1])


def p_params(p):
    '''params : exp COMMA params 
                | exp
    '''
    pass


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
